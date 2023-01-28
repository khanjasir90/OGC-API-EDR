class url:
    def __init__(self):
        self.base_url = "https://ogcie.iblsoft.com/edr/"
        self.collections = "conformance"
        self.conformance = "collections"

    def landing_urls(self) -> dict:
        return {"landing_url": self.base_url}
    
    def conformance_urls(self) -> dict:
        return {"conformance_url": self.base_url + self.conformance}

    def collection_metadata(self) -> dict:
        return {
            "collection_metadata_url": self.base_url+self.collections,
            "get_collection_metadata_url": "{base_url}{collections}/{collection_id}"
        }