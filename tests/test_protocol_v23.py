import struct
import unittest
import lz4.block

from protocol_v23 import (
    establish_packet,
    connection_key_packet,
    spawn_packet,
    target_packet,
    decrypt_server_packet,
)


class ProtocolV23Tests(unittest.TestCase):
    def test_establish_packet(self):
        self.assertEqual(establish_packet(), bytes.fromhex("fe17000000"))

    def test_connection_key_packet(self):
        self.assertEqual(
            connection_key_packet(),
            bytes.fromhex("ff9979000000000000"),
        )

    def test_spawn_packet(self):
        self.assertEqual(spawn_packet("TestBot"), b"\x00TestBot\x00")

    def test_spawn_rejects_null_character(self):
        with self.assertRaises(ValueError):
            spawn_packet("Test\x00Bot")

    def test_target_packet(self):
        self.assertEqual(
            target_packet(0, 0),
            bytes.fromhex("10000000000000000000000000"),
        )

    def test_target_rejects_out_of_range_integer(self):
        with self.assertRaises(struct.error):
            target_packet(2**40, 0)

    def test_decrypt_and_decompress_synthetic_packet(self):
        dks = 0x12345678
        eks = 0x7999
        inner = b"\x40synthetic-test"
        compressed = lz4.block.compress(inner, store_size=False)
        wrapper = b"\xff" + struct.pack("<I", len(inner)) + compressed

        key = struct.pack("<I", dks ^ eks)
        encrypted = bytes(
            b ^ key[i & 3] for i, b in enumerate(wrapper)
        )

        self.assertEqual(decrypt_server_packet(encrypted, dks, eks), inner)

    def test_rejects_invalid_wrapper(self):
        with self.assertRaises(ValueError):
            decrypt_server_packet(b"\x00\x00\x00\x00\x00", 1234)


if __name__ == "__main__":
    unittest.main(verbosity=2)
