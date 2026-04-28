from chatbot.data import training_data
from chatbot.model import build_and_train_model, load_model, predict_answer
def chat(model,vectorizer,unique_answers):
    """inicia el modo de comversacion"""
    print("\n🤖 chatbot listo. Ecribe 'salir' para terminar. \n")
    while True:
        user = input("Tú: ").strip()
        if user.lower() in {"salir","exit","quit"}:
            print("bot: !Hasta pronto¡")
            break
        response = predict_answer(model,vectorizer,unique_answers,user)
        print("bot: ", response)

def main():
    model, vectorizer,unique_answer = load_model()
    # Menu principal
    while True:
        print("\n==🤖 MENU PRINCIPAL DEL CHATBOT ==")
        print("1️⃣ Chatear con el modelo")
        print("2️⃣ Rentrenar el modelo ")
        print("3️⃣ salir")
        opcion=input("\n Elige una opcion (1-3); ").strip()
        if opcion =="1":
            if model is None:
                print("\n⚠️ No hay modelo entrenado. Entrenalo primero.")
            else:
                chat(model,vectorizer,unique_answer)

        elif opcion == "2":
            print("\n🔁 Rwntrena el modelo de los nuevos datos...")
            model,vectorizer,unique_answer=build_and_train_model(training_data)
            print("✅ Modelo actualizado correctamnete.")
        elif opcion =="3":
            print("\n👋 !Hasta luegoo¡")
            break
        else:
            print("\n ✖️ Opción no valida. Intenta nuevamente. ")
if __name__ == "__main__":
    main()