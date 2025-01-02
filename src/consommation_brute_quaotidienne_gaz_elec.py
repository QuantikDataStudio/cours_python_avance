import requests


def telecharger_data_gouv(dataset):
    url = f"https://tabular-api.data.gouv.fr/api/resources/{dataset}/data/?Date__exact='2024-10-31'"
    toutes_les_data = []

    print("Télécharger les données")
    while url:
        r = requests.get(url)
        r.raise_for_status()
        data = r.json()
        toutes_les_data += data['data']
        url = data['links'].get("next")
    return toutes_les_data
