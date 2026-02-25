"""Test db_connection.py module"""
import sys
sys.path.insert(0, '.')

print("[TEST] Testing db_connection.py module...")
print("=" * 70)

# Test 1: Syntax Check
print("\n[TEST 1] Syntax Validation...")
try:
    import py_compile
    py_compile.compile('src/etl/db_connection.py', doraise=True)
    print("[OK] ✓ Syntax is valid")
except Exception as e:
    print(f"[ERROR] ✗ Syntax error: {e}")
    sys.exit(1)

# Test 2: Import Test
print("\n[TEST 2] Module Import...")
try:
    from src.etl.db_connection import SnowflakeConnection, PostgreSQLConnection, ConnectionFactory
    print("[OK] ✓ All classes imported successfully")
    print("    - SnowflakeConnection")
    print("    - PostgreSQLConnection")
    print("    - ConnectionFactory")
except ImportError as e:
    print(f"[ERROR] ✗ Import error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Test 3: ConnectionFactory Creation
print("\n[TEST 3] ConnectionFactory Test...")
try:
    from src.config.config import Config
    
    # Test creating Snowflake connection object
    sf_conn = ConnectionFactory.create_connection('snowflake')
    print("[OK] ✓ Snowflake connection object created")
    
    # Test creating PostgreSQL connection object
    pg_conn = ConnectionFactory.create_connection('postgresql')
    print("[OK] ✓ PostgreSQL connection object created")
    
    # Test with unsupported database
    try:
        invalid_conn = ConnectionFactory.create_connection('mysql')
        print("[ERROR] ✗ Should have raised ValueError for unsupported database")
        sys.exit(1)
    except ValueError as ve:
        print(f"[OK] ✓ Correctly raised ValueError for unsupported database: {ve}")
    
except Exception as e:
    print(f"[ERROR] ✗ ConnectionFactory error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Test 4: Configuration Integration
print("\n[TEST 4] Configuration Integration...")
try:
    from src.config.config import get_config
    
    # Get development config
    dev_config = get_config('development')
    print("[OK] ✓ Development config loaded")
    
    # Create connection with config
    sf_conn_with_config = ConnectionFactory.create_connection('snowflake', dev_config)
    print("[OK] ✓ Snowflake connection created with config")
    
    # Verify connection properties
    assert sf_conn_with_config.config is not None
    print("[OK] ✓ Connection has config attached")
    
except Exception as e:
    print(f"[ERROR] ✗ Configuration integration error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Test 5: Method Availability
print("\n[TEST 5] Method Availability Check...")
try:
    from src.etl.db_connection import SnowflakeConnection, PostgreSQLConnection
    
    sf_conn = SnowflakeConnection()
    
    # Check Snowflake methods
    methods_sf = ['connect', 'execute_query', 'fetch_all', 'fetch_one', 'commit', 'rollback', 'close', '__enter__', '__exit__']
    for method in methods_sf:
        assert hasattr(sf_conn, method), f"Missing method: {method}"
    print(f"[OK] ✓ SnowflakeConnection has all {len(methods_sf)} required methods")
    
    pg_conn = PostgreSQLConnection()
    
    # Check PostgreSQL methods
    methods_pg = ['connect', 'execute_query', 'fetch_all', 'fetch_one', 'execute_many', 'commit', 'rollback', 'close', '__enter__', '__exit__']
    for method in methods_pg:
        assert hasattr(pg_conn, method), f"Missing method: {method}"
    print(f"[OK] ✓ PostgreSQLConnection has all {len(methods_pg)} required methods")
    
except AssertionError as ae:
    print(f"[ERROR] ✗ {ae}")
    sys.exit(1)
except Exception as e:
    print(f"[ERROR] ✗ Method check error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("\n" + "=" * 70)
print("RESULT: ALL TESTS PASSED ✓")
print("=" * 70)
print("\nDatabase Connection Module Status: READY")
print("\nSupported databases:")
print("  - Snowflake: SnowflakeConnection")
print("  - PostgreSQL: PostgreSQLConnection")
print("  - Factory pattern: ConnectionFactory.create_connection()")
print("\nExample usage:")
print("  from src.etl.db_connection import ConnectionFactory")
print("  conn = ConnectionFactory.create_connection('postgresql')")
print("  conn.connect()")
print("=" * 70)
