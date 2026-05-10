from scholarly import scholarly
import json
from datetime import datetime
import os

scholar_id = os.environ.get('GOOGLE_SCHOLAR_ID', 'P8hQuaYAAAAJ')

author: dict = scholarly.search_author_id(scholar_id)
scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
author['updated'] = str(datetime.now())

publications = {}
for publication in author.get('publications', []):
    publication['num_citations'] = int(publication.get('num_citations') or 0)
    publications[publication['author_pub_id']] = publication
author['publications'] = publications
author['citedby'] = int(author.get('citedby') or sum(
    publication['num_citations'] for publication in publications.values()
))

print(json.dumps(author, indent=2))
os.makedirs('results', exist_ok=True)
with open('results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldio_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author.get('citedby', 0)}",
}
with open('results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)
