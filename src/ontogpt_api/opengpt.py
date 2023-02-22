from fastapi import APIRouter, Request
from ontogpt.engines.spires_engine import SPIRESEngine
from src.ontogpt_api.config import logger

app = APIRouter()


@app.post("/extract")
def form_post(
    request: Request,
    datamodel: str = "drug.DrugMechanism",
    text: str = "According to its FDA labeling, acetaminophen's exact mechanism of action has not been fully established despite this, it is often categorized alongside NSAIDs (nonsteroidal anti-inflammatory drugs) due to its ability to inhibit the cyclooxygenase (COX) pathways.14 It is thought to exert central actions which ultimately lead to the alleviation of pain symptoms.14  One theory is that acetaminophen increases the pain threshold by inhibiting two isoforms of cyclooxygenase, COX-1 and COX-2, which are involved in prostaglandin (PG) synthesis. Prostaglandins are responsible for eliciting pain sensations.13 Acetaminophen does not inhibit cyclooxygenase in peripheral tissues and, therefore, has no peripheral anti-inflammatory effects. Though acetylsalicylic acid (aspirin) is an irreversible inhibitor of COX and directly blocks the active site of this enzyme, studies have shown that acetaminophen (paracetamol) blocks COX indirectly.24 Studies also suggest that acetaminophen selectively blocks a variant type of the COX enzyme that is unique from the known variants COX-1 and COX-2.6 This enzyme has been referred to as COX-3. The antipyretic actions of acetaminophen are likely attributed to direct action on heat-regulating centers in the brain, resulting in peripheral vasodilation, sweating, and loss of body heat.24",
):
    logger.info(f"Received request with schema {datamodel}")
    logger.info(f"Received request with text {text}")
    engine = SPIRESEngine(datamodel)
    ann = engine.extract_from_text(text)
    # logger.info(f"ANNOTATIONS: {ann}")
    return ann
