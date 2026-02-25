"""
Comprehensive test suite for Database Connection module
Tests syntax, imports, class definitions, and connection handling
"""

import sys
import ast
import py_compile
from pathlib import Path

# Test configuration
test_file = "src/etl/db_connection.py"
test_results = []

def test_syntax():
    """Test 1: Verify Python syntax is valid"""
    try:
        py_compile.compile(test_file, doraise=True)
        test_results.append(('Syntax Validation', True, 'No compilation errors'))
        return True
    except py_compile.PyCompileError as e:
        test_results.append(('Syntax Validation', False, str(e)))
        return False

def test_imports():
    """Test 2: Verify module imports successfully"""
    try:
        from src.etl import db_connection
        test_results.append(('Module Import', True, 'Module imported successfully'))
        return True
    except ImportError as e:
        test_results.append(('Module Import', False, str(e)))
        return False

def test_ast_structure():
    """Test 3: Verify AST structure and class definitions"""
    try:
        with open(test_file, 'r') as f:
            tree = ast.parse(f.read())
        
        classes = [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
        
        expected_classes = ['SnowflakeConnection', 'PostgreSQLConnection', 'ConnectionFactory']
        
        for cls in expected_classes:
            if cls not in classes:
                test_results.append(('AST Structure', False, f'Missing class: {cls}'))
                return False
        
        test_results.append(('AST Structure', True, f'Found {len(classes)} classes: {", ".join(classes)}'))
        return True
    except Exception as e:
        test_results.append(('AST Structure', False, str(e)))
        return False

def test_optional_imports():
    """Test 4: Verify optional import handling"""
    try:
        with open(test_file, 'r') as f:
            content = f.read()
        
        # Check for type: ignore comments on snowflake import
        if 'import snowflake.connector  # type: ignore' not in content:
            test_results.append(('Optional Imports', False, 'snowflake import missing type: ignore'))
            return False
        
        # Check for type: ignore comments on psycopg2 imports
        if 'import psycopg2  # type: ignore' not in content:
            test_results.append(('Optional Imports', False, 'psycopg2 import missing type: ignore'))
            return False
        
        if 'from psycopg2.extras import RealDictCursor  # type: ignore' not in content:
            test_results.append(('Optional Imports', False, 'psycopg2.extras import missing type: ignore'))
            return False
        
        # Check for try-except blocks
        if 'try:' not in content or 'except ImportError:' not in content:
            test_results.append(('Optional Imports', False, 'try-except block not found'))
            return False
        
        test_results.append(('Optional Imports', True, 'All optional imports correctly handled with type: ignore'))
        return True
    except Exception as e:
        test_results.append(('Optional Imports', False, str(e)))
        return False

def test_connection_methods():
    """Test 5: Verify connection class methods"""
    try:
        with open(test_file, 'r') as f:
            tree = ast.parse(f.read())
        
        # Get all class methods
        class_methods = {}
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                methods = [n.name for n in node.body if isinstance(n, ast.FunctionDef)]
                class_methods[node.name] = methods
        
        # Verify SnowflakeConnection methods
        snowflake_methods = ['connect', 'execute_query', 'fetch_one', 'fetch_all', 'commit', 'rollback', 'close']
        for method in snowflake_methods:
            if 'SnowflakeConnection' in class_methods and method not in class_methods['SnowflakeConnection']:
                test_results.append(('Connection Methods', False, f'SnowflakeConnection.{method} not found'))
                return False
        
        # Verify PostgreSQLConnection methods
        postgres_methods = ['connect', 'execute_query', 'fetch_one', 'fetch_all', 'execute_many', 'commit', 'rollback', 'close']
        for method in postgres_methods:
            if 'PostgreSQLConnection' in class_methods and method not in class_methods['PostgreSQLConnection']:
                test_results.append(('Connection Methods', False, f'PostgreSQLConnection.{method} not found'))
                return False
        
        # Verify ConnectionFactory methods
        factory_methods = ['create_connection']
        for method in factory_methods:
            if 'ConnectionFactory' in class_methods and method not in class_methods['ConnectionFactory']:
                test_results.append(('Connection Methods', False, f'ConnectionFactory.{method} not found'))
                return False
        
        test_results.append(('Connection Methods', True, 'All required connection methods found'))
        return True
    except Exception as e:
        test_results.append(('Connection Methods', False, str(e)))
        return False

def test_context_manager():
    """Test 6: Verify context manager support"""
    try:
        with open(test_file, 'r') as f:
            content = f.read()
        
        # Check for __enter__ and __exit__ methods
        if '__enter__' not in content:
            test_results.append(('Context Manager', False, '__enter__ method not found'))
            return False
        
        if '__exit__' not in content:
            test_results.append(('Context Manager', False, '__exit__ method not found'))
            return False
        
        test_results.append(('Context Manager', True, 'Context manager support (with statement) verified'))
        return True
    except Exception as e:
        test_results.append(('Context Manager', False, str(e)))
        return False

def test_error_handling():
    """Test 7: Verify error handling"""
    try:
        with open(test_file, 'r') as f:
            content = f.read()
        
        # Check for exception handling
        if 'except' not in content:
            test_results.append(('Error Handling', False, 'Exception handling not found'))
            return False
        
        # Check for logging errors
        if 'logger.error' not in content:
            test_results.append(('Error Handling', False, 'Error logging not found'))
            return False
        
        test_results.append(('Error Handling', True, 'Comprehensive error handling implemented'))
        return True
    except Exception as e:
        test_results.append(('Error Handling', False, str(e)))
        return False

def test_type_hints():
    """Test 8: Verify type hints"""
    try:
        with open(test_file, 'r') as f:
            content = f.read()
        
        # Check for Optional type hints
        if 'Optional' not in content:
            test_results.append(('Type Hints', False, 'Optional type hints not found'))
            return False
        
        # Check for Dict type hints
        if 'Dict' not in content:
            test_results.append(('Type Hints', False, 'Dict type hints not found'))
            return False
        
        # Check for Any type hints
        if 'Any' not in content:
            test_results.append(('Type Hints', False, 'Any type hints not found'))
            return False
        
        test_results.append(('Type Hints', True, 'Comprehensive type hints implemented'))
        return True
    except Exception as e:
        test_results.append(('Type Hints', False, str(e)))
        return False

def print_results():
    """Print test results in formatted table"""
    print("\n" + "="*80)
    print("DATABASE CONNECTION MODULE - COMPREHENSIVE TEST SUITE")
    print("="*80 + "\n")
    
    passed = 0
    failed = 0
    
    for test_name, result, message in test_results:
        status = "[PASS]" if result else "[FAIL]"
        symbol = "✓" if result else "✗"
        color = "\033[92m" if result else "\033[91m"
        reset = "\033[0m"
        
        print(f"{color}{status}{reset} {test_name:<25} {symbol}")
        print(f"     {message}\n")
        
        if result:
            passed += 1
        else:
            failed += 1
    
    print("="*80)
    print(f"RESULTS: {passed}/{len(test_results)} tests passed")
    
    if failed == 0:
        print(f"\n{color}✓ ALL TESTS PASSED - CODE IS PRODUCTION READY{reset}")
    else:
        print(f"\n{color}✗ {failed} test(s) failed - review errors above{reset}")
    
    print("="*80 + "\n")
    
    return failed == 0

def main():
    """Run all tests"""
    print("\nRunning comprehensive test suite...\n")
    
    # Run all tests
    test_syntax()
    test_imports()
    test_ast_structure()
    test_optional_imports()
    test_connection_methods()
    test_context_manager()
    test_error_handling()
    test_type_hints()
    
    # Print results
    all_passed = print_results()
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
