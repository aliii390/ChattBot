from langchain_mistralai.chat_models import ChatMistralAI
from langchain_mistralai.embeddings import MistralAIEmbeddings
import dotenv
import os
from typing import Optional
from datetime import datetime

class MistralAssistant:
    def __init__(self):
        dotenv.load_dotenv()
        self._check_api_key()
        self.llm = ChatMistralAI(
            temperature=0.7,  
            model="mistral-tiny" 
        )
        self.conversation_history = []
       

  


    def _check_api_key(self) -> None:
        """verif si la clé d'api existe"""
        if not os.getenv("MISTRAL_API_KEY"):
            raise ValueError("MISTRAL_API_KEY n'est pas définie dans le fichier .env")

    def ask(self, question: str) -> Optional[str]:
        try:
            response = self.llm.invoke(question)
            self.ajouter_a_l_historique(question, response.content)
            return response.content
        except Exception as e:
            print(f"❌ Erreur: {str(e)}")
            return None

    def ajouter_a_l_historique(self, question: str, answer: str) -> None:
        """ajoute une entrée à l'historique de conversation"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.conversation_history.append({
            "timestamp": timestamp,
            "question": question,
            "answer": answer
        })

    def enregistrer_historique(self, filename: str = "conversation.txt") -> None:
        """enregistre l'historique de conversation dans un fichier"""
        with open(filename, "w", encoding="utf-8") as f:
            for exchange in self.conversation_history:
                f.write(f"[{exchange['timestamp']}]\n")
                f.write(f"Question: {exchange['question']}\n")
                f.write(f"Réponse: {exchange['answer']}\n\n")

def main():
    """fonction principale"""
    print("🤖 Démarrage de 390LAND IA...")
    print("Tapez 'quit' pour quitter ou 'save' pour sauvegarder l'historique")
    
    assistant = MistralAssistant()
    
    while True:
        try:
            user_input = input("\n👤 Votre question: ").strip()
            
            if user_input.lower() == "quit":
                if assistant.conversation_history:
                    save = input("Voulez-vous sauvegarder l'historique ? (oui/non): ")
                    if save.lower() == "o":
                        assistant.enregistrer_historique()
                        print("👋 Au revoir!")
                        break
                   

                
                
            elif user_input.lower() == "save":
                assistant.enregistrer_historique()
                print("💾 Historique sauvegardé!")
                continue
                
            if user_input:
                response = assistant.ask(user_input)
                if response:
                    print(f"\n🤖 Assistant: {response}")
                    
        except KeyboardInterrupt:
            print("\n\n⚠️ Programme interrompu par l'utilisateur")
            break
        except Exception as e:
            print(f"\n❌ Une erreur est survenue: {str(e)}")

if __name__ == "__main__":
    main()