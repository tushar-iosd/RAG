from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

text = """from typing import List


class UserService:

    def __init__(self):
        self.users = []

    def create_user(self, name: str, email: str):
        user = {
            "name": name,
            "email": email,
            "active": True
        }

        self.users.append(user)
        return user

    def get_user(self, name: str):
        for user in self.users:
            if user["name"] == name:
                return user

        return None

    def get_active_users(self):
        active_users = []

        for user in self.users:
            if user["active"]:
                active_users.append(user)

        return active_users

    def deactivate_user(self, name: str):
        user = self.get_user(name)

        if user is None:
            return False

        user["active"] = False
        return True


def main():
    service = UserService()

    service.create_user("Tushar", "tushar@example.com")

    user = service.get_user("Tushar")

    if user:
        print(user)


if __name__ == "__main__":
    main()
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON, chunk_size=300,chunk_overlap=0
)

chunks = splitter.split_text(text)
print(chunks[2])