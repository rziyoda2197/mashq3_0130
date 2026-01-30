import random

RESPONSES = {
    "salom": ["Salom!", "Assalomu alaykum!", "Qalaysan?"],
    "yordam": ["Nima yordam kerak?", "Savolingizni yozing"],
    "xayr": ["Xayr!", "Ko‘rishguncha!"]
}

def chatbot():
    print("🤖 Chatbot ishga tushdi (chiqish: xayr)")

    while True:
        user = input("Siz: ").lower()

        for key, replies in RESPONSES.items():
            if key in user:
                print("Bot:", random.choice(replies))
                if key == "xayr":
                    return
                break
        else:
            print("Bot: Tushunmadim 🤔")

chatbot()
