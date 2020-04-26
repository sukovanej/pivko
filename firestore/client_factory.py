from google.cloud.firestore import Client


def firestore_client_factory():
    return Client()
