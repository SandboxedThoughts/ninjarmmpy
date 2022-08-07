from pathlib import Path

class Configure():
    
    def __init__(self, config: str = '.env', base_dir: str = Path().resolve(), ):
        self.config = config
        print(self.config)
        self.base_dir = base_dir
        print(self.base_dir)
        
        cfgf = Path(self.base_dir).joinpath(self.config)
        if not cfgf.exists():
            cfgf.touch()
