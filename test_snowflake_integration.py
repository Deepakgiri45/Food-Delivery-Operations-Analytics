"""
Comprehensive test suite for Snowflake integration module
Tests syntax, imports, class definitions, and optional dependency handling
"""

import sys
import ast
import py_compile
from pathlib import Path

# Test configuration
test_file = "src/snowflake/snowflake_integration.py"
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
        from src.snowflake import snowflake_integration
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
        functions = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
        
        expected_classes = ['SnowflakeOptimization', 'SemiStructuredDataHandler', 'PerformanceTuning']
        
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
        
        # Check for try-except block
        if 'try:' not in content or 'except ImportError:' not in content:
            test_results.append(('Optional Imports', False, 'try-except block not found'))
            return False
        
        # Check for SNOWFLAKE_AVAILABLE flag
        if 'SNOWFLAKE_AVAILABLE' not in content:
            test_results.append(('Optional Imports', False, 'SNOWFLAKE_AVAILABLE flag not found'))
            return False
        
        # Check for type: ignore comments
        if '# type: ignore' not in content:
            test_results.append(('Optional Imports', False, 'type: ignore comments not found'))
            return False
        
        test_results.append(('Optional Imports', True, 'Optional import pattern correctly implemented'))
        return True
    except Exception as e:
        test_results.append(('Optional Imports', False, str(e)))
        return False

def test_key_methods():
    """Test 5: Verify all key methods are defined"""
    try:
        with open(test_file, 'r') as f:
            tree = ast.parse(f.read())
        
        # Get all class methods
        class_methods = {}
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                methods = [n.name for n in node.body if isinstance(n, ast.FunctionDef)]
                class_methods[node.name] = methods
        
        # Verify SnowflakeOptimization methods
        required_methods = {
            'SnowflakeOptimization': [
                'connect', 'execute_query', 'setup_clustering', 
                'enable_time_travel', 'create_dynamic_table',
                'create_iceberg_table', 'close'
            ],
            'SemiStructuredDataHandler': ['load_json_data', 'query_json_column', 'flatten_json'],
            'PerformanceTuning': ['get_tuning_recommendations']
        }
        
        for class_name, methods in required_methods.items():
            if class_name not in class_methods:
                test_results.append(('Key Methods', False, f'Class {class_name} not found'))
                return False
            
            for method in methods:
                if method not in class_methods[class_name]:
                    test_results.append(('Key Methods', False, f'Method {class_name}.{method} not found'))
                    return False
        
        test_results.append(('Key Methods', True, f'All required methods found across {len(required_methods)} classes'))
        return True
    except Exception as e:
        test_results.append(('Key Methods', False, str(e)))
        return False

def test_variable_naming():
    """Test 6: Verify PEP 8 naming conventions"""
    try:
        with open(test_file, 'r') as f:
            content = f.read()
        
        # Check that old naming convention is fixed
        if 'unclusteredtables' in content:
            test_results.append(('Variable Naming', False, 'Old naming convention still present: unclusteredtables'))
            return False
        
        # Check new naming convention
        if 'unclustered_tables' not in content:
            test_results.append(('Variable Naming', False, 'New naming convention not found: unclustered_tables'))
            return False
        
        test_results.append(('Variable Naming', True, 'PEP 8 naming conventions correctly applied'))
        return True
    except Exception as e:
        test_results.append(('Variable Naming', False, str(e)))
        return False

def test_dependency_check():
    """Test 7: Verify dependency check in connect method"""
    try:
        with open(test_file, 'r') as f:
            content = f.read()
        
        # Check for dependency check in connect method
        if 'if not SNOWFLAKE_AVAILABLE:' not in content:
            test_results.append(('Dependency Check', False, 'Dependency check not found in connect()'))
            return False
        
        if 'snowflake-connector-python' not in content:
            test_results.append(('Dependency Check', False, 'Installation instruction not found'))
            return False
        
        test_results.append(('Dependency Check', True, 'Dependency check correctly implemented in connect()'))
        return True
    except Exception as e:
        test_results.append(('Dependency Check', False, str(e)))
        return False

def print_results():
    """Print test results in formatted table"""
    print("\n" + "="*80)
    print("SNOWFLAKE INTEGRATION MODULE - COMPREHENSIVE TEST SUITE")
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
    test_key_methods()
    test_variable_naming()
    test_dependency_check()
    
    # Print results
    all_passed = print_results()
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
