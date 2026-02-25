# Food Delivery Operations Analytics Platform

## 🚀 Project Overview

A comprehensive data engineering and analytics platform for food delivery operations. This platform integrates advanced data warehousing, real-time processing, ML capabilities, and interactive visualizations to provide deep insights into delivery operations, customer behavior, and business performance.

**Version:** 1.0.0  
**Status:** Production Ready  
**Last Updated:** February 2024

---

## 📋 Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                     DATA SOURCES                                     │
├─────────────────────────────────────────────────────────────────────┤
│  • Order Management System  • Delivery Tracking  • Customer CRM      │
│  • Payment Gateway         • Restaurant Catalog • Logistics Data     │
└──────────────┬──────────────────────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────────────────────┐
│              ETL/ELT PIPELINE LAYER                                 │
├─────────────────────────────────────────────────────────────────────┤
│  • Data Extraction      • Transformation    • Data Quality Checks    │
│  • Incremental Loading  • Change Data Capture (CDC)                 │
└──────────────┬──────────────────────────────────────────────────────┘
               │
        ┌──────┴──────┐
        ▼             ▼
┌──────────────┐  ┌──────────────────────────────────┐
│  BATCH PROC  │  │  STREAM PROCESSING (KafkaSpike)  │
│  • Spark     │  │  • Real-time Aggregation         │
│  • Analytics │  │  • Anomaly Detection             │
└──────────────┘  └──────────────────────────────────┘
        │             │
        └──────┬──────┘
               ▼
┌─────────────────────────────────────────────────────────────────────┐
│          DATA WAREHOUSE LAYER (Snowflake)                           │
├─────────────────────────────────────────────────────────────────────┤
│  • Star Schema Design      • Clustering & Partitioning             │
│  • Time Travel Support     • Search Optimization                    │
│  • Semi-Structured Data    • Dynamic Tables                        │
└──────────────┬──────────────────────────────────────────────────────┘
               │
    ┌──────────┴──────────┐
    ▼                     ▼
┌──────────────────┐  ┌─────────────────────────────┐
│  ANALYTICS LAYER │  │  GOVERNANCE LAYER           │
│  • SQL Queries   │  │  • RBAC Management         │
│  • CTE/Windows   │  │  • Data Masking            │
│  • Advanced Agg  │  │  • Audit Logging           │
└──────────────────┘  │  • Encryption              │
                      └─────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────────────────────┐
│         VISUALIZATION & BI LAYER                                    │
├─────────────────────────────────────────────────────────────────────┤
│  • Streamlit Dashboard     • Plotly Graphs        • Real-time Feeds │
│  • KPI Metrics             • Trend Analysis       • Alerts          │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 🏗️ Project Structure

```
Food Delivery Operations Analytics/
├── src/
│   ├── __init__.py
│   ├── config/
│   │   ├── config.py              # Configuration management
│   │   ├── snowflake_config.json  # Snowflake setup
│   │   └── __init__.py
│   ├── schema/
│   │   └── 01_star_schema.sql     # Data warehouse schema
│   ├── sql/
│   │   └── 02_advanced_queries.sql # CTE, Window Functions, etc.
│   ├── etl/
│   │   ├── db_connection.py       # Database connections
│   │   ├── data_generator.py      # Sample data generation
│   │   ├── etl_pipeline.py        # ETL orchestration
│   │   └── __init__.py
│   ├── spark/
│   │   ├── batch_processor.py     # Spark batch processing
│   │   ├── streaming_processor.py # Spark Structured Streaming
│   │   └── __init__.py
│   ├── snowflake/
│   │   ├── snowflake_integration.py # Snowflake optimization
│   │   └── __init__.py
│   ├── security/
│   │   ├── rbac_and_masking.py    # RBAC, Data Masking, Governance
│   │   └── __init__.py
│   ├── dashboard/
│   │   ├── app.py                 # Streamlit dashboard
│   │   └── __init__.py
│   ├── utils/
│   │   ├── helper_functions.py    # Utility functions
│   │   └── __init__.py
│   └── tests/
│       └── __init__.py
├── docs/
│   ├── ARCHITECTURE.md
│   ├── API_REFERENCE.md
│   └── DEPLOYMENT.md
├── data/                           # Sample data directory
├── logs/                           # Application logs
├── .env                            # Environment variables
├── requirements.txt                # Python dependencies
├── README.md                       # This file
├── setup.py                        # Package setup
└── pytest.ini                      # Test configuration
```

---

## 🎯 Key Features

### 1. **Data Warehouse Design (Star/Snowflake Schema)**
- Optimized dimensional modeling
- Fact tables: Orders, Deliveries, Menu Items
- Dimension tables: Date, Restaurant, Customer, Delivery Partner, Payment Method, Zone
- Support for slowly changing dimensions (SCD)

### 2. **Advanced SQL Queries**
- Common Table Expressions (CTEs) for complex hierarchies
- Window Functions: ROW_NUMBER, RANK, DENSE_RANK, LAG, LEAD
- Aggregate Functions with OVER clauses
- Partitioning and Clustering strategies
- Performance-optimized indexes

### 3. **Python-based ETL/ELT**
- Extract from multiple sources (JSON, CSV, APIs)
- Transform with data validation and cleaning
- Load with error handling and recovery
- Incremental and full load capabilities
- Data quality checks and reconciliation

### 4. **Apache Spark Processing**
- **Batch Processing**: Historical data analysis and aggregations
- **Streaming**: Real-time event processing with Structured Streaming
- Data quality checks and anomaly detection
- Distributed computation for large-scale data

### 5. **Snowflake Integration**
- Dynamic tables for real-time analysis
- Clustering for query optimization
- Time Travel for data recovery
- Search optimization for complex queries
- Zero-copy cloning for testing
- Semi-structured data handling (JSON/Parquet)

### 6. **Security & Governance**
- **RBAC**: Role-based access control (Admin, Analyst, Manager, Viewer, Developer)
- **Data Masking**: Automatic masking of PII (emails, phones, names)
- **Audit Logging**: Complete audit trail of all data access
- **Encryption**: Data encryption at rest and in transit
- **Compliance**: GDPR and data privacy support

### 7. **Performance Tuning**
- Query optimization techniques
- Index strategies
- Partitioning for faster queries
- Materialized views for pre-computed metrics
- Cost optimization recommendations

### 8. **Interactive Dashboard**
- Real-time metrics and KPIs
- Restaurant performance analytics
- Payment method analysis
- Delivery performance tracking
- Customer segmentation insights
- Time-series trending

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Snowflake account
- PostgreSQL (optional, for local testing)
- Apache Spark 3.5+
- Kafka (optional, for streaming)

### Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd "Food Delivery Operations Analytics"
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment**
```bash
cp .env.example .env
# Edit .env with your credentials
```

5. **Initialize database**
```bash
python src/schema/setup_database.py
```

---

## 📊 Data Schema

### Dimension Tables

#### dim_date
Time dimension with hierarchical data (year, quarter, month, week, day)

#### dim_restaurant
Restaurant information with ratings, location, and operational hours

#### dim_customer
Customer profiles with segmentation and lifetime value metrics

#### dim_delivery_partner
Delivery partner details with performance metrics

#### dim_payment_method
Payment methods supported in the platform

#### dim_zone
Geographic zones for delivery management

### Fact Tables

#### fact_orders
Order transactions with amounts, status, and timestamps

#### fact_deliveries
Delivery records with time, distance, and rating metrics

#### fact_menu_items
Menu item performance with sales and popularity scores

---

## 🔧 Usage Examples

### Running ETL Pipeline
```python
from src.etl.etl_pipeline import ETLPipeline
from src.config.config import Config

config = Config()
pipeline = ETLPipeline(config, db_type='snowflake')
pipeline.connect()
stats = pipeline.execute_pipeline('data')
```

### Spark Batch Processing
```python
from src.spark.batch_processor import SparkBatchProcessor

processor = SparkBatchProcessor()
orders_df = processor.load_parquet('data/orders.parquet')
daily_metrics = processor.calculate_daily_metrics(orders_df)
daily_metrics.show()
```

### Spark Streaming
```python
from src.spark.streaming_processor import SparkStreamingProcessor

processor = SparkStreamingProcessor()
orders_stream = processor.read_kafka_stream('localhost:9092', 'orders')
metrics = processor.calculate_streaming_metrics(orders_stream)
processor.write_to_console(metrics, "order_metrics")
```

### Running Dashboard
```bash
streamlit run src/dashboard/app.py
```

### Executing SQL Queries
```bash
snowsql -c <connection_name> -f src/sql/02_advanced_queries.sql
```

---

## 🔐 Security Features

### Role-Based Access Control
```python
from src.security.rbac_and_masking import RBACManager

# Check permissions
if RBACManager.check_permission('ANALYST', 'SELECT'):
    # Allow data access
```

### Data Masking
```python
from src.security.rbac_and_masking import DataMaskingEngine, DataGovernance

# Mask sensitive data
masked_email = DataMaskingEngine.mask_email('customer@example.com')
# Output: cu***@example.com

# Log access
governance = DataGovernance()
governance.log_access('user123', 'fact_orders', 'SELECT', 'SUCCESS')
```

---

## 📈 Performance Optimization

### Query Optimization
- Use clustering keys for filtered queries
- Implement search optimization for complex predicates
- Leverage materialized views for frequent aggregations
- Use result caching for repeated queries

### Snowflake Optimization
```python
from src.snowflake.snowflake_integration import SnowflakeOptimization

optimizer = SnowflakeOptimization()
optimizer.setup_clustering('fact_orders', ['order_date', 'restaurant_id'])
optimizer.enable_time_travel('fact_orders', 90)
recommendations = PerformanceTuning.get_tuning_recommendations(connection)
```

---

## 🧪 Testing

Run tests using pytest:
```bash
pytest src/tests/ -v --cov=src
```

---

## 📚 Documentation

- **[Architecture Documentation](docs/ARCHITECTURE.md)** - Detailed system architecture
- **[API Reference](docs/API_REFERENCE.md)** - Complete API documentation
- **[Deployment Guide](docs/DEPLOYMENT.md)** - Production deployment steps
- **[SQL Queries](src/sql/02_advanced_queries.sql)** - Advanced query examples

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License.

---

## 📞 Support

For issues, questions, or suggestions:
- Create an issue on GitHub
- Email: support@fooddeliveryanalytics.com
- Documentation: https://docs.fooddeliveryanalytics.com

---

## 🙏 Acknowledgments

- Snowflake for data warehousing platform
- Apache Spark for distributed processing
- Streamlit for interactive dashboards
- PostgreSQL for local testing
- The open-source community

---

**Last Updated:** February 2024  
**Maintained by:** Data Engineering Team
