from exa_py import Exa
import os

from dotenv import load_dotenv

load_dotenv()


class ExaSearchTool:

    def __init__(self):

        self.client = Exa(
            api_key=os.getenv("EXA_API_KEY")
        )

    def search(
        self,
        query,
        num_results=5
    ):

        try:

            response = self.client.search_and_contents(
                query,
                num_results=num_results
            )

            results = []

            for item in response.results:

                results.append({

                    "title": item.title,

                    "url": item.url,

                    "content": item.text[:1200]
                })

            return results

        except Exception as e:

            print("EXA SEARCH ERROR:", str(e))

            return []