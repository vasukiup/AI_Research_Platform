class ClaimExtractor:

    def extract(self, findings):

        claims = []

        for item in findings:

            content = item.get("content", "")

            sentences = content.split(".")

            for sentence in sentences[:3]:

                cleaned = sentence.strip()

                if len(cleaned) > 50:

                    claims.append(cleaned)

        return claims[:10]