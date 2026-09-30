import asyncio
import logging
from telegram import Bot

TOKEN = "8859364166:AAF0adeK4fr4ByL_8immgdC_knINUu79IFI"
CHAT_ID = "8671185091"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)


def analyze_otc_market(asset, candle_prices):
    current_price = candle_prices[-1]
    support_level = min(candle_prices[:-1])
    resistance_level = max(candle_prices[:-1])

    if current_price <= support_level:
        return "CALL 🟢 (صعود)"
    elif current_price >= resistance_level:
        return "PUT 🔴 (هبوط)"

    return None


async def run_bot():
    await bot.send_message(
        chat_id=CHAT_ID,
        text="🚀 **تم تشغيل بوت تحليل الـ OTC بنجاح!**\nالاستراتيجية: 3 دقائق (M3).",
        parse_mode="Markdown",
    )

    while True:
        asset_name = "EUR/USD OTC"
        sample_prices = [1.0820, 1.0825, 1.0830, 1.0815, 1.0815]

        signal = analyze_otc_market(asset_name, sample_prices)

        if signal:
            msg = (
                f"📊 **إشارة تداول OTC جديدة**\n\n"
                f"🔹 الزوج: `{asset_name}`\n"
                f"🎯 الاتجاه: **{signal}**\n"
                f"⏱ الوقت: 3 دقائق (M3)\n"
                f"💡 الملاحظة: ارتداد من مستوى رئيسي"
            )
            await bot.send_message(
                chat_id=CHAT_ID, text=msg, parse_mode="Markdown"
            )

        # فحص السوق كل 3 دقائق
        await asyncio.sleep(180)


if __name__ == "__main__":
    asyncio.run(run_bot())
