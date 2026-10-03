try:
    from pydantic import BaseModel
except ImportError:  # pragma: no cover
    from pydantic.main import BaseModel

from datetime import datetime


# Model untuk menerima request prediksi dari user
class PredictionRequest(BaseModel):
    visit_day: str



# Model untuk response hasil prediksi
class PredictionResponse(BaseModel):
    status: str
    prediction: int



# Model data histori jumlah pengunjung
class VisitorHistory(BaseModel):
    id: int
    visit_date: str
    visit_day: str
    visitor_total: int



# Model data hasil prediksi
class PredictionResult(BaseModel):
    id: int
    visitor_history_id: int
    visit_day: str
    prediction_value: int
    created_at: datetime