class BaseTool:
    name: str = "BaseTool"
    description: str = "Abstract tool; subclass must implement _run()"

    def run(self, query: str) -> str:
        return self._run(query)

    def _run(self, query: str) -> str:
        raise NotImplementedError("Must implement _run()")
