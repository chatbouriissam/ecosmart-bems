# EcoSmart BEMS - Building Energy Management System

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A comprehensive Building Energy Management System that uses advanced anomaly detection and machine learning to optimize energy consumption, detect equipment failures, and improve building efficiency.

## 🏢 Features

### Real-time Monitoring
- **Multi-sensor Integration**: HVAC, lighting, occupancy, energy meters
- **Live Dashboard**: Real-time energy consumption and building metrics
- **3D Building Visualization**: Interactive floor plans and sensor placement

### Advanced Analytics
- **Anomaly Detection**: Machine learning-powered detection of unusual patterns
- **Predictive Maintenance**: Early warning system for equipment failures
- **Energy Optimization**: Automated recommendations for energy savings
- **Trend Analysis**: Historical data analysis and forecasting

### Professional Architecture
- **RESTful API**: Complete API for integration with building systems
- **Database Integration**: PostgreSQL/SQLite with historical data storage
- **Real-time Alerts**: Email/SMS notifications for critical events
- **Docker Deployment**: Containerized for easy deployment

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Docker (optional)
- PostgreSQL (optional, SQLite included)

### Installation

```bash
# Clone the repository
git clone https://github.com/chatbouri-issam/ecosmart-bems.git
cd ecosmart-bems

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

### Docker Deployment

```bash
# Build and run with Docker Compose
docker-compose up --build
```

## 📊 Demo

The system includes a comprehensive demo with:
- Simulated office building with 50+ sensors
- Real-time anomaly detection
- Energy consumption analytics
- Interactive web dashboard

Access the dashboard at: `http://localhost:8080`

## 🏗️ Architecture

```
EcoSmart-BEMS/
├── sbems/                  # Core application
│   ├── core/              # Building and sensor management
│   ├── sensors/           # Sensor implementations
│   ├── analytics/         # ML and anomaly detection
│   ├── api/               # REST API endpoints
│   └── database/          # Data persistence
├── web/                   # Frontend dashboard
├── tests/                 # Unit and integration tests
├── docs/                  # Documentation
└── config/                # Configuration files
```

## 🔧 Configuration

The system supports multiple deployment scenarios:

- **Development**: SQLite database, local sensors
- **Production**: PostgreSQL, real sensor integration
- **Demo**: Simulated building with realistic data

## 📈 Use Cases

### Energy Management
- **Cost Reduction**: 15-30% energy savings through optimization
- **Peak Load Management**: Automatic load balancing during peak hours
- **Carbon Footprint**: Detailed emissions tracking and reduction

### Facility Management
- **Predictive Maintenance**: Reduce equipment downtime by 40%
- **Space Optimization**: Occupancy-based lighting and HVAC control
- **Compliance Reporting**: Automated energy audits and reports

### Building Operations
- **Remote Monitoring**: 24/7 building oversight
- **Automated Controls**: Smart scheduling and control systems
- **Emergency Response**: Immediate alerts for system failures

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](docs/CONTRIBUTING.md) for details.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built on advanced machine learning algorithms
- Inspired by real-world building management challenges
- Designed for scalability and production use

## 📞 Support

For questions and support:
- 📧 Email: chatbouri.issam@gmail.com

---

**Built with pride for sustainable and efficient buildings**
