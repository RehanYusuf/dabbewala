# 🍱 Dabbewala – Tiffin Delivery Order Management API

A REST API built using **Python, FastAPI, and SQLModel** to manage tiffin delivery orders, track their delivery statuses, and generate daily order summaries.

Dabbewala provides a simple backend system for managing the journey of a tiffin order, from preparation to final delivery.

---

## 📌 About the Project

Imagine running a tiffin delivery service where multiple customers place orders every day.

You need a system to:

- 📝 Register new customer orders.
- 📦 Store order details and delivery addresses.
- 🚚 Track the current status of each order.
- 🔍 Find orders based on their delivery status.
- 📊 Generate daily reports showing how many orders are in each delivery stage.

**Dabbewala** is a backend application designed to handle these operations through REST API endpoints.

It uses FastAPI to handle HTTP requests and SQLModel with SQLite to store and retrieve order information.

## ✨ Features

- 📝 **Create Orders:** Register new orders with customer names, delivery addresses, and ordered items.
- 📋 **Retrieve Orders:** Fetch all available orders from the database.
- 🚚 **Order Status Tracking:** Organize orders into different delivery stages.
- 🔍 **Status Filtering:** Retrieve orders based on their current status.
- 📄 **Pagination:** Use skip and limit parameters to retrieve orders in manageable batches.
- 📊 **Daily Order Summary:** Generate reports showing the total number of orders and their distribution across different statuses.
- 🗄️ **Database Integration:** Store order information using SQLite and SQLModel.
- ⚡ **Interactive API Documentation:** Explore and test endpoints using automatically generated Swagger documentation.

## 🔄 How Does It Work?

The application follows a simple workflow:

1. 📝 A customer places a tiffin order.
2. 📤 The order details are submitted through an API request.
3. 🗄️ FastAPI processes the request and stores the order in the SQLite database.
4. 🚚 The order is associated with a delivery status.
5. 🔍 Orders can be retrieved and filtered through API endpoints.
6. 📊 The statistics endpoint generates a daily summary of orders.

## 🚚 Order Delivery Lifecycle

Each order can have one of the following statuses:

| Status | Description |
|---|---|
| 🟡 `preparing` | The tiffin is being prepared. |
| 📦 `picked_up` | The order has been picked up for delivery. |
| 🚴 `in_transit` | The order is on its way to the customer. |
| 🟢 `delivered` | The order has been successfully delivered. |

These statuses are represented using a Python Enum, ensuring consistent status values throughout the application.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| 🐍 Python | Main programming language |
| ⚡ FastAPI | Building REST API endpoints |
| 🗄️ SQLModel | Database models and database operations |
| 💾 SQLite | Storing order information |
| 📦 Pydantic | Data validation through SQLModel |
| 🚀 Uvicorn | Running the FastAPI application |
| 📖 Swagger UI | Interactive API documentation |

## 📂 Project Structure

```text
dabbewala/
│
├── routes/
│   ├── orders.py       # Order creation and retrieval
│   └── stats.py        # Daily order statistics
│
├── database.py         # Database connection and sessions
├── models.py           # Order models and schemas
├── main.py             # FastAPI application entry point
│
├── dabbewala.db        # SQLite database
│
└── README.md           # Project documentation
```

### Understanding the Files

- **main.py:** Initializes the FastAPI application, creates database tables, and registers API routers.
- **database.py:** Configures the SQLite database connection and provides database sessions.
- **models.py:** Defines the Order model, OrderStatus enum, and request schemas.
- **routes/orders.py:** Contains endpoints for creating and retrieving orders.
- **routes/stats.py:** Contains the endpoint for generating daily order summaries.
- **dabbewala.db:** Stores the application's order records.

## 🚀 Getting Started

Follow these steps to run the project locally.

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/RehanYusuf/dabbewala.git
```

### 2️⃣ Navigate to the Project Directory

```bash
cd dabbewala
```

### 3️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment.

**Windows:**

```bash
venv\Scripts\activate
```

**macOS / Linux:**

```bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies

Install the required Python packages:

```bash
pip install fastapi uvicorn sqlmodel
```

### 5️⃣ Start the Application

Run the following command:

```bash
uvicorn main:app --reload
```

The server will start at:

http://127.0.0.1:8000

The SQLite database tables are created automatically when the application starts.

## 📖 API Documentation

FastAPI automatically generates interactive API documentation using Swagger UI.

Once the server is running, open:

**Swagger UI:**

http://127.0.0.1:8000/docs

**ReDoc:**

http://127.0.0.1:8000/redoc

You can explore the available endpoints, submit requests, and inspect their responses directly from your browser.

## 🔌 API Endpoints

The application currently provides the following endpoints:

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Welcome endpoint |
| GET | `/health` | Check API health |
| POST | `/orders/` | Create a new order |
| GET | `/orders/` | Retrieve orders |
| GET | `/stats/daily` | Generate daily order statistics |

### 1. Create a New Order

**Endpoint:** `POST /orders/`

Creates a new tiffin delivery order.

**Example Request:**

```json
{
  "customer_name": "Rahul Sharma",
  "delivery_address": "Sector 62, Noida",
  "items": "2 Veg Thalis"
}
```

The application stores the order in the database and assigns its default status as `preparing`.

### 2. Retrieve All Orders

**Endpoint:** `GET /orders/`

Returns the available orders stored in the database.

**Optional Query Parameters:**

| Parameter | Description | Default |
|---|---|---|
| `status` | Filter orders by delivery status | None |
| `created_date` | Filter by creation date | None |
| `skip` | Number of records to skip | 0 |
| `limit` | Maximum number of records to retrieve | 20 |

**Example Request:**

```http
GET /orders/?status=preparing&skip=0&limit=10
```

This request retrieves up to 10 orders with the `preparing` status.

### 3. Generate Daily Order Statistics

**Endpoint:** `GET /stats/daily`

Generates a summary of orders created on a particular date.

If no date is provided, the application uses the current date.

**Example Request:**

```http
GET /stats/daily?summary_date=2026-11-24
```

**Example Response:**

```json
{
  "date": "2026-11-24",
  "total_orders": 20,
  "by_status": {
    "preparing": 5,
    "picked_up": 4,
    "in_transit": 6,
    "delivered": 5
  }
}
```

*The response above is illustrative and not actual database output.*

The summary helps understand how many orders are currently in each delivery stage.

### 4. Health Check

**Endpoint:** `GET /health`

Checks whether the API is responding.

**Example Response:**

```json
{
  "status": "ok"
}
```

## 📊 Database Design

The application uses an SQLite database with an Order table.

### Order Table

| Column | Description |
|---|---|
| `id` | Unique order identifier |
| `customer_name` | Name of the customer |
| `delivery_address` | Customer's delivery address |
| `items` | Ordered tiffin items |
| `status` | Current delivery status |
| `created_at` | Order creation timestamp |
| `updated_at` | Last update timestamp |

SQLModel is used to define the database model and interact with SQLite through Python.

## 📚 Concepts Implemented

This project helped explore several important backend development concepts:

- REST API architecture and HTTP methods.
- FastAPI routers and endpoint creation.
- Dependency injection using `Depends()`.
- Database sessions and CRUD fundamentals.
- SQLModel database models and schemas.
- Python Enum for managing order statuses.
- Query parameters for filtering and pagination.
- SQL aggregate functions such as `COUNT()`.
- Date-based database queries.
- Application lifecycle management using lifespan events.

## 🔮 Future Improvements

Some features that can be added to make the application more comprehensive:

- ✏️ Add APIs to update order details and delivery statuses.
- ❌ Add an endpoint to cancel or delete orders.
- 👤 Introduce customer and delivery partner authentication.
- 🔐 Implement role-based access control.
- 📍 Add delivery partner assignment and delivery tracking.
- 📈 Build a dashboard for visualizing daily and monthly statistics.
- 🧪 Add automated API testing using Pytest.
- 🐳 Containerize the application using Docker.

## ⚠️ Project Status

This is a learning-oriented backend project demonstrating REST API development, database integration, order management, and basic reporting using FastAPI.

The current implementation supports order creation, order retrieval, status filtering, pagination, and daily statistics. Additional order management features are planned for future development.

## 👨‍💻 Author

**Yusuf Rehan**

- 🐙 GitHub: [@RehanYusuf](https://github.com/RehanYusuf)
- 💼 LinkedIn: [Yusuf Rehan](https://www.linkedin.com/in/yusuf-rehan-10a611253/)

---

⭐ If you find this project useful, consider giving the repository a star!

