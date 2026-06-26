from fastapi import APIRouter, HTTPException
from app.services.dashboard_service import get_dashboard_data

router = APIRouter()


@router.get("/{user_id}")
def get_dashboard(user_id: int):

    dashboard_data = get_dashboard_data(user_id)

    if dashboard_data is None:
        raise HTTPException(
            status_code=404,
            detail="Dashboard data not found"
        )

    return {
        "success": True,
        "message": "Dashboard fetched successfully",
        "data": dashboard_data
    }


@router.get("/")
def dashboard_home():
    return {
        "message": "Dashboard API Working Successfully"
    }