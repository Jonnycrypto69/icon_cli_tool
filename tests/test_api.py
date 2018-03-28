import os
import unittest

import eth_keyfile

from icxcli import icx
from icxcli.icx import wallet, utils
from icxcli.icx.utils import validate_key_store_file

TEST_DIR = os.path.dirname(os.path.abspath(__file__))


class TestAPI(unittest.TestCase):
    """
    Test that execute the api about Wallet
    """
    def setUp(self):
        # Remove used file.
        file_path = os.path.join(TEST_DIR, "test_keystore.txt")
        if os.path.isfile(file_path):
            os.remove(file_path)

    def test_create_wallet_case0(self):
        """Test for create_wallet function.
        Case when created wallet successfully.
        """
        # Given
        password="Adas21312**"
        file_path=os.path.join(TEST_DIR, "test_keystore.txt")

        # When
        try:
            wallet_info = icx.wallet.create_wallet(password, file_path)

            # Then
            prefix = wallet_info.address[0:2]
            self.assertEqual(prefix, "hx")

        except icx.FilePathIsWrong:
            self.assertFalse(True)
        except icx.PasswordIsNotAcceptable:
            self.assertFalse(True)
        except icx.NoPermissionToWriteFile:
            self.assertFalse(True)

        # Remove used file.
        os.remove(file_path)

    def test_create_wallet_case1(self):
        """Test for create_wallet function.
        Case when user enters a directory that does not exist.
        """
        # Given
        password = "Adas21312**"
        wallet_name = "wname"
        file_path = os.path.join(TEST_DIR,'unknown', "test_keystore.txt")

        # When
        try:
            wallet_info = icx.wallet.create_wallet(password, file_path)

        # Then
        except icx.FilePathIsWrong:
            self.assertTrue(True)

    def test_create_wallet_case2(self):
        """Test for create_wallet function.
        Case when user enters a invalid password.
        """
        # Given
        password = "123 4"
        wallet_name = "wname"
        file_path=os.path.join(TEST_DIR,"unknown_folder" ,"test_keystore.txt")

        # When
        try:
            wallet_info = icx.wallet.create_wallet(password, file_path)

        # Then
        except icx.PasswordIsNotAcceptable:
            self.assertTrue(True)

    def test_create_wallet_case3(self):
        """Test for create_wallet function.
        Case when user enters a directory without permission to write file.
        """
        # Given
        password = "Adas21312**"
        wallet_name = "wname"
        file_path=os.path.join("/", "test_keystore.txt")

        # When
        try:
            wallet_info = icx.wallet.create_wallet(password, file_path)
        # Then
        except icx.NoPermissionToWriteFile:
            self.assertTrue(True)

    def test_create_wallet_case4(self):
        """Test for create_wallet function.
        Case when user tries to overwrite keystore file.
        """
        # Given
        password = "Adas21312**"
        wallet_name = "wname"
        file_path = os.path.join(TEST_DIR, "test_keystore.txt")

        # When
        wallet_info = icx.wallet.create_wallet(password, file_path)

        try:
            wallet_info2 = icx.wallet.create_wallet(password, file_path)

        # Then
        except icx.FileExists: # Raise exception that file exists.
            self.assertTrue(True)

            # Remove used file.
            os.remove(file_path)

    def test_create_wallet_case5(self):
        """Test for create_wallet function.
        Case when user entered the file, not a key_store_file.
        """
        # Given
        file_path = os.path.join(TEST_DIR, "not_a_key_store_file.txt")
        password = "Adas21312**"

        # When
        try:
            wallet_info = validate_key_store_file(file_path)
        except icx.NotAKeyStoreFile:
            self.assertTrue(True)

    def test_created_store_key_file(self):
        """Check the file is saved in the correct format.
        """
        # Given
        password = "Adas21312**"
        wallet_name = "wname"
        file_path=os.path.join(TEST_DIR, "test_keystore.txt")

        # When
        try:
            wallet_info = icx.wallet.create_wallet(password, file_path)

        # Then
            self.assertTrue(utils.validate_key_store_file(file_path))
        except:
            self.assertTrue(False) # Never happen this case.


if __name__ == "__main__":
    unittest.main()