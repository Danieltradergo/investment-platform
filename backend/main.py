from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import uvicorn

app = FastAPI(
    title="Investment Platform API",
    description="Professional Investment Platform with Portfolio Management",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data Models
class Portfolio(BaseModel):
    id: Optional[int] = None
    name: str
    balance: float
    created_at: Optional[datetime] = None

class Asset(BaseModel):
    id: Optional[int] = None
    portfolio_id: int
    symbol: str
    quantity: float
    purchase_price: float
    current_price: float

class Transaction(BaseModel):
    id: Optional[int] = None
    portfolio_id: int
    asset_symbol: str
    transaction_type: str  # buy, sell
    quantity: float
    price: float
    timestamp: Optional[datetime] = None

# Sample data
portfolios = [
    {"id": 1, "name": "Main Portfolio", "balance": 50000, "created_at": datetime.now()},
    {"id": 2, "name": "Growth Portfolio", "balance": 30000, "created_at": datetime.now()}
]

assets = [
    {"id": 1, "portfolio_id": 1, "symbol": "AAPL", "quantity": 10, "purchase_price": 150, "current_price": 180},
    {"id": 2, "portfolio_id": 1, "symbol": "GOOGL", "quantity": 5, "purchase_price": 2800, "current_price": 3000}
]

# Endpoints
@app.get("/")
def read_root():
    return {"message": "Investment Platform API", "version": "1.0.0"}

@app.get("/api/portfolios", response_model=List[Portfolio])
def get_portfolios():
    """Get all portfolios"""
    return portfolios

@app.post("/api/portfolios", response_model=Portfolio)
def create_portfolio(portfolio: Portfolio):
    """Create new portfolio"""
    portfolio_dict = portfolio.dict()
    portfolio_dict["id"] = len(portfolios) + 1
    portfolio_dict["created_at"] = datetime.now()
    portfolios.append(portfolio_dict)
    return portfolio_dict

@app.get("/api/portfolios/{portfolio_id}", response_model=Portfolio)
def get_portfolio(portfolio_id: int):
    """Get specific portfolio"""
    for p in portfolios:
        if p["id"] == portfolio_id:
            return p
    return {"error": "Portfolio not found"}

@app.get("/api/assets", response_model=List[Asset])
def get_assets():
    """Get all assets"""
    return assets

@app.post("/api/assets", response_model=Asset)
def create_asset(asset: Asset):
    """Create new asset"""
    asset_dict = asset.dict()
    asset_dict["id"] = len(assets) + 1
    assets.append(asset_dict)
    return asset_dict

@app.get("/api/health")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "investment-platform-api"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
