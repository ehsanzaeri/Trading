import time
import random
import string
from mnemonic import Mnemonic
from bitcoinlib.wallets import Wallet
from bitcoinlib.services.services import Service

# تابع برای تولید عبارت بازیابی تصادفی از لیست BIP-39
def generate_random_mnemonic():
    mnemo = Mnemonic("english")
    mnemonic_phrase = mnemo.generate(strength=128)
    return mnemonic_phrase

# تابع برای بررسی صحت عبارت بازیابی
def validate_mnemonic(mnemonic_phrase):
    mnemo = Mnemonic("english")
    return mnemo.check(mnemonic_phrase)

# تابع برای تولید نام تصادفی برای کیف پول
def generate_wallet_name():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))

# تابع برای تبدیل عبارت بازیابی به آدرس بیت کوین
def mnemonic_to_wallet(mnemonic_phrase):
    wallet_name = generate_wallet_name()
    wallet = Wallet.create(wallet_name, keys=mnemonic_phrase, network='bitcoin')
    address = wallet.get_key().address
    return address, wallet

# تابع برای بررسی موجودی بیت کوین
def check_balance(wallet):
    # بررسی موجودی با استفاده از متد get_balance برای کیف پول
    balance = wallet.balance()
    return balance / 1e8  # تبدیل موجودی به بیت کوین

# حلقه تا زمانی که موجودی غیر صفر باشد
while True:
    random_mnemonic = generate_random_mnemonic()
    print(f"Generated Mnemonic: {random_mnemonic}")

    if validate_mnemonic(random_mnemonic):
        print("Mnemonic is valid!")

        wallet_address, wallet = mnemonic_to_wallet(random_mnemonic)
        print("Bitcoin Wallet Address:", wallet_address)

        balance = check_balance(wallet)

        print(f"Bitcoin Wallet Balance: {balance} BTC")

        if balance > 0:
            print("Non-zero balance found, stopping.")
            break
    else:
        print("Mnemonic is invalid!\n")

    print("Waiting 360 seconds before next check...\n")
    time.sleep(360)
