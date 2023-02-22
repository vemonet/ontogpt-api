from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from oaklib.utilities.apikey_manager import set_apikey_value
from ontogpt.engines.spires_engine import SPIRESEngine
from src.ontogpt_api.config import settings

set_apikey_value("openai", settings.OPENAI_APIKEY)
set_apikey_value("bioportal", settings.BIOPORTAL_APIKEY)


app = FastAPI(
    title="OntoGPT API",
    description="""API to extract informations from text using OntoGPT.

[Source code](https://github.com/vemonet/ontogpt-api)
""",
    license_info={"name": "MIT license", "url": "https://opensource.org/licenses/MIT"},
    contact={
        "name": "Vincent Emonet",
        "email": "vincent.emonet@gmail.com",
        "url": "https://github.com/vemonet/ontogpt-api",
    },
)


@app.post("/extract")
def form_post(
    request: Request,
    datamodel: str = "drug.DrugMechanism",
    text: str = "According to its FDA labeling, acetaminophen's exact mechanism of action has not been fully established despite this, it is often categorized alongside NSAIDs (nonsteroidal anti-inflammatory drugs) due to its ability to inhibit the cyclooxygenase (COX) pathways.14 It is thought to exert central actions which ultimately lead to the alleviation of pain symptoms.14  One theory is that acetaminophen increases the pain threshold by inhibiting two isoforms of cyclooxygenase, COX-1 and COX-2, which are involved in prostaglandin (PG) synthesis. Prostaglandins are responsible for eliciting pain sensations.13 Acetaminophen does not inhibit cyclooxygenase in peripheral tissues and, therefore, has no peripheral anti-inflammatory effects. Though acetylsalicylic acid (aspirin) is an irreversible inhibitor of COX and directly blocks the active site of this enzyme, studies have shown that acetaminophen (paracetamol) blocks COX indirectly.24 Studies also suggest that acetaminophen selectively blocks a variant type of the COX enzyme that is unique from the known variants COX-1 and COX-2.6 This enzyme has been referred to as COX-3. The antipyretic actions of acetaminophen are likely attributed to direct action on heat-regulating centers in the brain, resulting in peripheral vasodilation, sweating, and loss of body heat.24"
    # text: str = "According to its FDA labeling, acetaminophen's exact mechanism of action has not been fully established despite this, it is often categorized alongside NSAIDs (nonsteroidal anti-inflammatory drugs) due to its ability to inhibit the cyclooxygenase (COX) pathways.14 It is thought to exert central actions which ultimately lead to the alleviation of pain symptoms.14  One theory is that acetaminophen increases the pain threshold by inhibiting two isoforms of cyclooxygenase, COX-1 and COX-2, which are involved in prostaglandin (PG) synthesis. Prostaglandins are responsible for eliciting pain sensations.13 Acetaminophen does not inhibit cyclooxygenase in peripheral tissues and, therefore, has no peripheral anti-inflammatory effects. Though acetylsalicylic acid (aspirin) is an irreversible inhibitor of COX and directly blocks the active site of this enzyme, studies have shown that acetaminophen (paracetamol) blocks COX indirectly.24 Studies also suggest that acetaminophen selectively blocks a variant type of the COX enzyme that is unique from the known variants COX-1 and COX-2.6 This enzyme has been referred to as COX-3. The antipyretic actions of acetaminophen are likely attributed to direct action on heat-regulating centers in the brain, resulting in peripheral vasodilation, sweating, and loss of body heat.24 The exact mechanism of action of this drug is not fully understood at this time, but future research may contribute to deeper knowledge"
):
    print(f"Received request with schema {datamodel}")
    print(f"Received request with text {text}")
    engine = SPIRESEngine(datamodel)
    ann = engine.extract_from_text(text)
    # print(f"Got {ann}")
    return ann


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", include_in_schema=False)
def redirect_root_to_docs():
    """Redirect the route / to /docs"""
    return RedirectResponse(url="/docs")
