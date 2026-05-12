from src.configs.default_config import DefaultConfig
from src.configs.production_config import ProductionConfig


class TestProductionConfig:
    def test_debug_is_false(self) -> None:
        config: ProductionConfig = ProductionConfig()

        assert config.DEBUG is False

    def test_env_is_production(self) -> None:
        config: ProductionConfig = ProductionConfig()

        assert config.ENV == "production"

    def test_testing_is_false(self) -> None:
        config: ProductionConfig = ProductionConfig()

        assert config.TESTING is False

    def test_is_subclass_of_default_config(self) -> None:
        assert issubclass(ProductionConfig, DefaultConfig)

    def test_inherits_tz_from_default(self) -> None:
        config: ProductionConfig = ProductionConfig()

        assert config.TZ is not None
        assert config.TZ != ""
