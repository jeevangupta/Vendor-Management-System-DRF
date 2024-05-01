
# Vendor Management System with Performance Metrics

- Objective:
    Develop a Vendor Management System using Django and Django REST Framework. This system will handle vendor profiles, track purchase orders, and calculate vendor performance metrics.

  NOTE: Use Python version >= 3.9

## Setup Instructions

1. Clone the repository:
    - git clone (https://github.com/jeevangupta/Vendor-Management-System-DRF.git)
    - cd Vendor-Management-System-DRF

2. Create a virtual environment:
   - python3 -m venv env
   - source ./env/bin/activate

3. Install dependencies:
   - pip install -r requirements.txt

4. Run database migrations:
   - cd VMSproject
   - python3 manage.py migrate

5. Start the development server:
   - python3 manage.py runserver
  
## API Endpoints

  **Superuser creation and Token generation**
  - POST /api-token-auth/: Will create a super user and return an auth token to be used for below API call to work
  
  **Vendor Profile Management**
  
  - POST /api/vendors/: Create a new vendor.
  - GET /api/vendors/: List all vendors.
  - GET /api/vendors/{vendor_id}/: Retrieve a specific vendor's details.
  - PUT /api/vendors/{vendor_id}/: Update a vendor's details.
  - DELETE /api/vendors/{vendor_id}/: Delete a vendor.

  **Purchase Order Tracking**
  - POST /api/purchase_orders/: Create a purchase order.
  - GET /api/purchase_orders/: List all purchase orders with an option to filter by the vendor.
  - GET /api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order.
  - PUT /api/purchase_orders/{po_id}/: Update a purchase order.
  - DELETE /api/purchase_orders/{po_id}/: Delete a purchase order.

  **Vendor Performance Evaluation**
  - GET /api/vendors/{vendor_id}/performance: Retrieve a vendor's performance metrics.

  **Update Acknowledgment**
  - POST /api/purchase_orders/{po_id}/acknowledge for vendors to acknowledge POs.

## API Endpoint Testing Using Postman
  - use the below link to get access to the postman collection to make all API end point call and test the project.
  (https://documenter.getpostman.com/view/33959556/2sA3JDiRJo)
  
