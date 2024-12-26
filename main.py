import os
import requests
from telegram import Bot

# Bot token ve chat ID'si ortam değişkenlerinden alınır
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
BASE_URL = "https://www.resmigazete.gov.tr/"  # Resmi Gazete URL

def check_resmi_gazete():
    # Resmi Gazete içeriğini tarama (örnek)
    keywords = [
        "iş hukuku", "ticaret kanunu", "borçlar kanunu",
        "basın ilan", "resmi ilan ve reklam", 
        "radyo ve televizyon", "yayın hizmetleri", "reklam"
    ]

    response = requests.get(BASE_URL)
    response.raise_for_status()
    content = response.text

    found_sentences = []
    for keyword in keywords:
        if keyword in content:
            found_sentences.append(f"'{keyword}' bulundu.")

    return "\n".join(found_sentences) if found_sentences else "Hiçbir anahtar kelime bulunamadı."

def main():
    bot = Bot(token=BOT_TOKEN)
    try:
        result = check_resmi_gazete()
        bot.send_message(chat_id=CHAT_ID, text=result)
    except Exception as e:
        bot.send_message(chat_id=CHAT_ID, text=f"Bir hata oluştu: {e}")

if __name__ == "__main__":
    main()
