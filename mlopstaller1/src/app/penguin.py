from pydantic import BaseModel

class Penguin(BaseModel):
    studyName: str = "PAL0708"
    SampleNumber: int = 1
    Region: str "Anvers"
    Island: str "Torgersen"
    Stage: str "Adult, 1 Egg Stage"
    IndividualID: str "N1A1"
    ClutchCompletion: str = "Yes",
    DateEgg: str = "11/11/87",
    CulmenLength_mm: float = 39.1,
    CulmenDepth_mm: float = 18.7,
    FlipperLength_mm: float = 181.0,
    BodyMass_g: float = 3750.0,
    Sex: str = "MALE"
    Delta_15_N: str = "NaN"
    Delta_13_C: str = "NaN"
    Comments: str = "Not enough.."
    