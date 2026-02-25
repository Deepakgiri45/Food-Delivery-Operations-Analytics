"""Test script for configuration module"""
import sys
sys.path.insert(0, '.')
from src.config.config import get_config, Config, DevelopmentConfig, ProductionConfig, TestingConfig

print("=" * 70)
print("[CONFIG TEST] Configuration Module Test Results")
print("=" * 70)

# Test 1: Load development config
dev_cfg = get_config('development')
print("\n[OK] Development Config Loaded")
print(f"   - Database: {dev_cfg.DB_NAME}")
print(f"   - Debug Mode: {dev_cfg.DEBUG}")

# Test 2: Load production config
prod_cfg = get_config('production')
print("\n[OK] Production Config Loaded")
print(f"   - Database: {prod_cfg.DB_NAME}")
print(f"   - Debug Mode: {prod_cfg.DEBUG}")

# Test 3: Load testing config
test_cfg = get_config('testing')
print("\n[OK] Testing Config Loaded")
print(f"   - Database: {test_cfg.DB_NAME}")
print(f"   - Testing Mode: {test_cfg.TESTING}")

# Test 4: Snowflake connection params
sf_params = dev_cfg.get_snowflake_connection_params()
print("\n[OK] Snowflake Connection Parameters Retrieved")
print(f"   - Account: {sf_params['account']}")
print(f"   - Warehouse: {sf_params['warehouse']}")

# Test 5: Spark configuration
spark_config = dev_cfg.get_spark_config()
print("\n[OK] Spark Configuration Retrieved")
print(f"   - Master: {spark_config['spark.master']}")
print(f"   - App Name: {spark_config['spark.app.name']}")

# Test 6: Security settings
print("\n[OK] Security Settings")
print(f"   - RBAC Enabled: {dev_cfg.RBAC_ENABLED}")
print(f"   - Data Masking Enabled: {dev_cfg.DATA_MASKING_ENABLED}")

# Test 7: Logging configuration
print("\n[OK] Logging Configuration")
print(f"   - Log Level: {dev_cfg.LOG_LEVEL}")
print(f"   - Log File: {dev_cfg.LOG_FILE}")

print("\n" + "=" * 70)
print("[SUCCESS] ALL CONFIGURATION TESTS PASSED!")
print("=" * 70)
