#!/usr/bin/env python
"""
Project Structure Validation Script
Verifies that all required files and directories have been created
"""

import os
import sys
from pathlib import Path


def validate_project_structure():
    """Validate that all project files exist"""
    
    base_dir = Path(__file__).parent
    
    # Define required directories
    required_dirs = [
        'src',
        'src/config',
        'src/schema',
        'src/sql',
        'src/etl',
        'src/spark',
        'src/snowflake',
        'src/security',
        'src/dashboard',
        'src/utils',
        'src/tests',
        'docs',
        'data',
        'logs'
    ]
    
    # Define required files
    required_files = {
        # Configuration
        '.env': 'Environment variables',
        'src/config/config.py': 'Configuration module',
        'src/config/snowflake_config.json': 'Snowflake configuration',
        
        # Schema
        'src/schema/01_star_schema.sql': 'Star schema design',
        
        # SQL
        'src/sql/02_advanced_queries.sql': 'Advanced SQL queries',
        
        # ETL
        'src/etl/db_connection.py': 'Database connections',
        'src/etl/data_generator.py': 'Sample data generation',
        'src/etl/etl_pipeline.py': 'ETL orchestration',
        
        # Spark
        'src/spark/batch_processor.py': 'Spark batch processing',
        'src/spark/streaming_processor.py': 'Spark streaming',
        
        # Snowflake
        'src/snowflake/snowflake_integration.py': 'Snowflake integration',
        
        # Security
        'src/security/rbac_and_masking.py': 'RBAC and data masking',
        
        # Dashboard
        'src/dashboard/app.py': 'Streamlit dashboard',
        
        # Utils
        'src/utils/helper_functions.py': 'Utility functions',
        
        # Documentation
        'README.md': 'Project README',
        'docs/ARCHITECTURE.md': 'Architecture documentation',
        'docs/DEPLOYMENT.md': 'Deployment guide',
        'PROJECT_SUMMARY.md': 'Project summary',
        
        # Setup
        'setup.py': 'Package setup',
        'main.py': 'Main entry point',
        'requirements.txt': 'Dependencies',
        'pytest.ini': 'Pytest configuration',
        '.gitignore': 'Git ignore rules',
    }
    
    # Check directories
    print("=" * 70)
    print("📁 DIRECTORY VALIDATION")
    print("=" * 70)
    
    all_dirs_found = True
    for dir_path in required_dirs:
        full_path = base_dir / dir_path
        if full_path.exists() and full_path.is_dir():
            print(f"✅ {dir_path:<40} EXISTS")
        else:
            print(f"❌ {dir_path:<40} MISSING")
            all_dirs_found = False
    
    # Check files
    print("\n" + "=" * 70)
    print("📄 FILE VALIDATION")
    print("=" * 70)
    
    all_files_found = True
    for file_path, description in required_files.items():
        full_path = base_dir / file_path
        if full_path.exists() and full_path.is_file():
            file_size = full_path.stat().st_size
            size_kb = file_size / 1024
            print(f"✅ {file_path:<40} ({size_kb:>6.1f} KB) - {description}")
        else:
            print(f"❌ {file_path:<40} MISSING - {description}")
            all_files_found = False
    
    # Statistics
    print("\n" + "=" * 70)
    print("📊 PROJECT STATISTICS")
    print("=" * 70)
    
    # Count Python files
    py_files = list(base_dir.rglob('*.py'))
    py_lines = 0
    for py_file in py_files:
        if '__pycache__' not in str(py_file):
            try:
                with open(py_file, 'r', encoding='utf-8', errors='ignore') as f:
                    py_lines += len(f.readlines())
            except:
                pass
    
    # Count SQL files
    sql_files = list(base_dir.rglob('*.sql'))
    sql_lines = 0
    for sql_file in sql_files:
        try:
            with open(sql_file, 'r', encoding='utf-8') as f:
                sql_lines += len(f.readlines())
        except:
            pass
    
    # Count documentation
    doc_files = list(base_dir.rglob('*.md'))
    doc_lines = 0
    for doc_file in doc_files:
        try:
            with open(doc_file, 'r', encoding='utf-8') as f:
                doc_lines += len(f.readlines())
        except:
            pass
    
    print(f"Python Files:        {len([f for f in py_files if '__pycache__' not in str(f)]):<5} files")
    print(f"Python Lines:        {py_lines:<5} lines")
    print(f"SQL Files:           {len(sql_files):<5} files")
    print(f"SQL Lines:           {sql_lines:<5} lines")
    print(f"Documentation:       {len(doc_files):<5} files")
    print(f"Documentation Lines: {doc_lines:<5} lines")
    print(f"Total Lines:         {py_lines + sql_lines + doc_lines:<5} lines")
    
    # Summary
    print("\n" + "=" * 70)
    print("✨ VALIDATION SUMMARY")
    print("=" * 70)
    
    if all_dirs_found and all_files_found:
        print("✅ ALL VALIDATIONS PASSED!")
        print(f"\n📦 Project Status: COMPLETE & READY FOR USE")
        print(f"\n🚀 Next Steps:")
        print(f"   1. Install dependencies: pip install -r requirements.txt")
        print(f"   2. Configure environment: Edit .env file")
        print(f"   3. Run initialization: python main.py --full-init")
        print(f"   4. Start dashboard: streamlit run src/dashboard/app.py")
        return 0
    else:
        print("❌ VALIDATION FAILED!")
        if not all_dirs_found:
            print("   - Some directories are missing")
        if not all_files_found:
            print("   - Some files are missing")
        return 1


if __name__ == "__main__":
    sys.exit(validate_project_structure())
