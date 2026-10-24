import struct
import lz4.block


def decrypt_server_packet(data: bytes, dks: int, eks: int = 0x7999) -> bytes:
    key = struct.pack("<I", (dks ^ eks) & 0xFFFFFFFF)
    decrypted = bytes(b ^ key[i & 3] for i, b in enumerate(data))

    if len(decrypted) < 5 or decrypted[0] != 0xFF:
        raise ValueError("Invalid encrypted packet wrapper")

    size = struct.unpack_from("<I", decrypted, 1)[0]
    return lz4.block.decompress(
        decrypted[5:], uncompressed_size=size
    )


def establish_packet():
    return struct.pack("<BI", 0xFE, 23)


def connection_key_packet(eks=0x7999):
    return struct.pack("<BQ", 0xFF, eks)


def spawn_packet(nickname):
    if "\0" in nickname:
        raise ValueError("Nickname cannot contain null")
    return b"\x00" + nickname.encode("utf-8") + b"\x00"


def target_packet(x, y):
    return struct.pack("<Biii", 0x10, x, y, 0)


if __name__ == "__main__":
    print("Establish:", establish_packet().hex())
    print("Connection key:", connection_key_packet().hex())
    print("Spawn:", spawn_packet("TestBot").hex())
    print("Target:", target_packet(0, 0).hex())
