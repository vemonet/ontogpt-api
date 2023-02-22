from fastapi import APIRouter, Request
from ontogpt.engines.spires_engine import SPIRESEngine
from src.ontogpt_api.config import logger

app = APIRouter()


@app.post("/extract")
def post_extract(
    request: Request,
    datamodel: str = "drug.DrugMechanism",
    text: str = "According to its FDA labeling, acetaminophen's exact mechanism of action has not been fully established despite this, it is often categorized alongside NSAIDs (nonsteroidal anti-inflammatory drugs) due to its ability to inhibit the cyclooxygenase (COX) pathways.14 It is thought to exert central actions which ultimately lead to the alleviation of pain symptoms.14  One theory is that acetaminophen increases the pain threshold by inhibiting two isoforms of cyclooxygenase, COX-1 and COX-2, which are involved in prostaglandin (PG) synthesis. Prostaglandins are responsible for eliciting pain sensations.13 Acetaminophen does not inhibit cyclooxygenase in peripheral tissues and, therefore, has no peripheral anti-inflammatory effects. Though acetylsalicylic acid (aspirin) is an irreversible inhibitor of COX and directly blocks the active site of this enzyme, studies have shown that acetaminophen (paracetamol) blocks COX indirectly.24 Studies also suggest that acetaminophen selectively blocks a variant type of the COX enzyme that is unique from the known variants COX-1 and COX-2.6 This enzyme has been referred to as COX-3. The antipyretic actions of acetaminophen are likely attributed to direct action on heat-regulating centers in the brain, resulting in peripheral vasodilation, sweating, and loss of body heat.24",
):
    logger.info(f"Received request with schema: {datamodel}")
    logger.info(f"Received request with text: {text}")
    engine = SPIRESEngine(datamodel)
    ann = engine.extract_from_text(text)
    # logger.info(f"ANNOTATIONS: {ann}")
    return ann



# Example returned object:

opengpt_returned_obj = {
  "input_id": None,
  "input_title": None,
  "input_text": "Clozapine is indicated for the treatment of severely ill patients with schizophrenia who fail to respond adequately to standard antipsychotic treatment",
  "raw_completion_output": "disease: schizophrenia;\ndrug: Clozapine;\nmechanism_links: Clozapine:treats:schizophrenia;schizophrenia:treated_by:Clozapine.",
  "prompt": "Split the following piece of text into fields in the following format:\n\nsubject: <the value for subject>\npredicate: <the value for predicate>\nobject: <the value for object>\n\n\nText:\nschizophrenia:treated_by:Clozapine.\n\n===\n\n",
  "extracted_object": {
    "disease": "schizophrenia;",
    "drug": "Clozapine;",
    "mechanism_links": [
      {
        "subject": "MESH:D003024",
        "predicate": "biolink:treats",
        "object": "MESH:D012559"
      },
      {
        "subject": "MESH:D012559",
        "predicate": "biolink:treated_by",
        "object": "MESH:D003024"
      }
    ],
    "references": [],
    "source_text": None
  },
  "named_entities": [
    {
      "id": "CHEBI:3766",
      "label": "Clozapine"
    },
    {
      "id": "biolink:treats",
      "label": "treats"
    },
    {
      "id": "MESH:D012559",
      "label": "schizophrenia"
    },
    {
      "id": "MESH:D012559",
      "label": "schizophrenia"
    },
    {
      "id": "biolink:treated_by",
      "label": "treated_by"
    },
    {
      "id": "CHEBI:3766",
      "label": "Clozapine"
    }
  ]
}


collaboratory_returned_obj = {
  "entities": [
    {
      "index": "Amantadine hydrochloride:0:0:24",
      "text": "Amantadine hydrochloride",
      "type": "ChemicalEntity",
      "start": 0,
      "end": 24,
      "props": [],
      "curies": [
        {
          "curie": "UMLS:C0936072",
          "label": "Amantadine Hydrochloride",
          "altLabel": "AMANTADINE HYDROCHLORIDE"
        },
        {
          "curie": "PUBCHEM.COMPOUND:64150",
          "label": "Amantadine hydrochloride",
          "altLabel": None
        },
        {
          "curie": "PUBCHEM.COMPOUND:19031614",
          "label": "AMANTADINE HYDROCHLORIDE",
          "altLabel": "Amantadine hydrochloride"
        },
        {
          "curie": "HMDB:HMDB0245807",
          "label": "Amantadine hydrochloride",
          "altLabel": "Hydrochloride, amantadine"
        },
        {
          "curie": "PUBCHEM.COMPOUND:2130",
          "label": "Amantadine hydrochloride",
          "altLabel": "Hydrochloride, amantadine"
        },
        {
          "curie": "PUBCHEM.COMPOUND:163285254",
          "label": "Amantadine-d15 Hydrochloride",
          "altLabel": None
        },
        {
          "curie": "UMLS:C2684460",
          "label": "amantadine hydrochloride 100 MG",
          "altLabel": None
        },
        {
          "curie": "UMLS:C4720105",
          "label": "Amantadine Hydrochloride Tablets",
          "altLabel": None
        },
        {
          "curie": "UMLS:C2684458",
          "label": "amantadine hydrochloride 10 MG/ML",
          "altLabel": None
        },
        {
          "curie": "UMLS:C4720215",
          "label": "Amantadine Hydrochloride Capsules",
          "altLabel": None
        }
      ],
      "id_curie": "UMLS:C0936072",
      "id_label": "Amantadine Hydrochloride",
      "id_uri": "http://identifiers.org/umls/C0936072"
    },
    {
      "index": "idiopathic Parkinson’s disease:1:68:98",
      "text": "idiopathic Parkinson’s disease",
      "type": "DiseaseOrPhenotypicFeature",
      "start": 68,
      "end": 98,
      "props": [],
      "curies": []
    },
    {
      "index": "postencephalitic parkinsonism:2:120:149",
      "text": "postencephalitic parkinsonism",
      "type": "DiseaseOrPhenotypicFeature",
      "start": 120,
      "end": 149,
      "props": [],
      "curies": [
        {
          "curie": "MONDO:0001945",
          "label": "postencephalitic Parkinsonism",
          "altLabel": "postencephalitic parkinsonism"
        }
      ],
      "id_curie": "MONDO:0001945",
      "id_label": "postencephalitic Parkinsonism",
      "id_uri": "http://purl.obolibrary.org/obo/MONDO_0001945"
    },
    {
      "index": "parkinsonism:3:166:178",
      "text": "parkinsonism",
      "type": "DiseaseOrPhenotypicFeature",
      "start": 166,
      "end": 178,
      "props": [],
      "curies": [
        {
          "curie": "DOID:0080855",
          "label": "Parkinsonism",
          "altLabel": "Parkinsonism"
        },
        {
          "curie": "MONDO:0021095",
          "label": "PARKINSONISM",
          "altLabel": "parkinsonism"
        },
        {
          "curie": "UMLS:C2939151",
          "label": "FH: Parkinsonism",
          "altLabel": "Family history: Parkinsonism"
        },
        {
          "curie": "MONDO:0009839",
          "label": "PSP-parkinsonism",
          "altLabel": "progressive supranuclear palsy-parkinsonism syndrome"
        },
        {
          "curie": "UMLS:C5548370",
          "label": "PSP-parkinsonism",
          "altLabel": "Progressive supranuclear palsy parkinsonism syndrome"
        },
        {
          "curie": "UMLS:C0752101",
          "label": "PARKINSONISM EXPER",
          "altLabel": "EXPER PARKINSONISM"
        },
        {
          "curie": "UMLS:C0270729",
          "label": "drugs; parkinsonism",
          "altLabel": "parkinsonism due to drug"
        },
        {
          "curie": "MONDO:0006966",
          "label": "PARKINSONISM SECOND",
          "altLabel": "SECOND PARKINSONISM"
        },
        {
          "curie": "UMLS:C1843796",
          "label": "Parkinsonism (later)",
          "altLabel": None
        },
        {
          "curie": "MONDO:0005180",
          "label": "Primary parkinsonism",
          "altLabel": "Primary Parkinsonism"
        }
      ],
      "id_curie": "DOID:0080855",
      "id_label": "Parkinsonism",
      "id_uri": "http://purl.obolibrary.org/obo/DOID_0080855"
    },
    {
      "index": "injury to the nervous system:4:196:224",
      "text": "injury to the nervous system",
      "type": "DiseaseOrPhenotypicFeature",
      "start": 196,
      "end": 224,
      "props": [],
      "curies": []
    },
    {
      "index": "carbon monoxide:5:228:243",
      "text": "carbon monoxide",
      "type": "ChemicalEntity",
      "start": 228,
      "end": 243,
      "props": [],
      "curies": [
        {
          "curie": "PUBCHEM.COMPOUND:281",
          "label": "Carbon monoxide",
          "altLabel": "Carbon Monoxide"
        },
        {
          "curie": "UMLS:C0007018",
          "label": "Carbon monoxide",
          "altLabel": "Carbon Monoxide"
        },
        {
          "curie": "UMLS:C4520712",
          "label": "Carbon monoxide",
          "altLabel": "Carbon monoxide measurement"
        },
        {
          "curie": "UMLS:C1268558",
          "label": "O15 Carbon Monoxide",
          "altLabel": "[15O]Carbon Monoxide"
        },
        {
          "curie": "UMLS:C1874024",
          "label": "AIR/CARBON MONOXIDE",
          "altLabel": None
        },
        {
          "curie": "PUBCHEM.COMPOUND:6432172",
          "label": "carbon monoxide(1+)",
          "altLabel": "CO(1+)"
        },
        {
          "curie": "UMLS:C1268564",
          "label": "Carbon Monoxide C-11",
          "altLabel": "Carbon Monoxide, C-11"
        },
        {
          "curie": "UMLS:C0007020",
          "label": "CARBON MONOXIDE POIS",
          "altLabel": "POIS CARBON MONOXIDE"
        },
        {
          "curie": "PUBCHEM.COMPOUND:10313038",
          "label": "CARBON MONOXIDE C-11",
          "altLabel": "Carbon monoxide c-11"
        },
        {
          "curie": "PUBCHEM.COMPOUND:10129878",
          "label": "CARBON MONOXIDE, O-15",
          "altLabel": "Carbon monoxide, O-15"
        }
      ],
      "id_curie": "PUBCHEM.COMPOUND:281",
      "id_label": "Carbon monoxide",
      "id_uri": "http://identifiers.org/pubchem.compound/281"
    }
  ],
  "relations": [
    {
      "sentence": "Amantadine hydrochloride capsules are indicated in the treatment of idiopathic Parkinson’s disease (Paralysis Agitans), postencephalitic parkinsonism and symptomatic parkinsonism which may follow injury to the nervous system by carbon monoxide intoxication.",
      "entity1": "Amantadine hydrochloride",
      "entity2": "idiopathic Parkinson’s disease",
      "type": "treats"
    },
    {
      "sentence": "Amantadine hydrochloride capsules are indicated in the treatment of idiopathic Parkinson’s disease (Paralysis Agitans), postencephalitic parkinsonism and symptomatic parkinsonism which may follow injury to the nervous system by carbon monoxide intoxication.",
      "entity1": "Amantadine hydrochloride",
      "entity2": "postencephalitic parkinsonism",
      "type": "treats"
    },
    {
      "sentence": "Amantadine hydrochloride capsules are indicated in the treatment of idiopathic Parkinson’s disease (Paralysis Agitans), postencephalitic parkinsonism and symptomatic parkinsonism which may follow injury to the nervous system by carbon monoxide intoxication.",
      "entity1": "Amantadine hydrochloride",
      "entity2": "parkinsonism",
      "type": "treats"
    },
    {
      "sentence": "Amantadine hydrochloride capsules are indicated in the treatment of idiopathic Parkinson’s disease (Paralysis Agitans), postencephalitic parkinsonism and symptomatic parkinsonism which may follow injury to the nervous system by carbon monoxide intoxication.",
      "entity1": "Amantadine hydrochloride",
      "entity2": "injury to the nervous system",
      "type": "treats"
    },
    {
      "sentence": "Amantadine hydrochloride capsules are indicated in the treatment of idiopathic Parkinson’s disease (Paralysis Agitans), postencephalitic parkinsonism and symptomatic parkinsonism which may follow injury to the nervous system by carbon monoxide intoxication.",
      "entity1": "Amantadine hydrochloride",
      "entity2": "carbon monoxide",
      "type": "treats"
    },
    {
      "sentence": "Amantadine hydrochloride capsules are indicated in the treatment of idiopathic Parkinson’s disease (Paralysis Agitans), postencephalitic parkinsonism and symptomatic parkinsonism which may follow injury to the nervous system by carbon monoxide intoxication.",
      "entity1": "idiopathic Parkinson’s disease",
      "entity2": "carbon monoxide",
      "type": "associated_with"
    },
    {
      "sentence": "Amantadine hydrochloride capsules are indicated in the treatment of idiopathic Parkinson’s disease (Paralysis Agitans), postencephalitic parkinsonism and symptomatic parkinsonism which may follow injury to the nervous system by carbon monoxide intoxication.",
      "entity1": "postencephalitic parkinsonism",
      "entity2": "carbon monoxide",
      "type": "positively_correlated_with"
    },
    {
      "sentence": "Amantadine hydrochloride capsules are indicated in the treatment of idiopathic Parkinson’s disease (Paralysis Agitans), postencephalitic parkinsonism and symptomatic parkinsonism which may follow injury to the nervous system by carbon monoxide intoxication.",
      "entity1": "parkinsonism",
      "entity2": "carbon monoxide",
      "type": "positively_correlated_with"
    },
    {
      "sentence": "Amantadine hydrochloride capsules are indicated in the treatment of idiopathic Parkinson’s disease (Paralysis Agitans), postencephalitic parkinsonism and symptomatic parkinsonism which may follow injury to the nervous system by carbon monoxide intoxication.",
      "entity1": "injury to the nervous system",
      "entity2": "carbon monoxide",
      "type": "positively_correlated_with"
    }
  ],
  "statements": [
    {
      "s": {
        "index": "Amantadine hydrochloride:0:0:24",
        "text": "Amantadine hydrochloride",
        "type": "ChemicalEntity",
        "start": 0,
        "end": 24,
        "props": [],
        "curies": [
          {
            "curie": "UMLS:C0936072",
            "label": "Amantadine Hydrochloride",
            "altLabel": "AMANTADINE HYDROCHLORIDE"
          },
          {
            "curie": "PUBCHEM.COMPOUND:64150",
            "label": "Amantadine hydrochloride",
            "altLabel": None
          },
          {
            "curie": "PUBCHEM.COMPOUND:19031614",
            "label": "AMANTADINE HYDROCHLORIDE",
            "altLabel": "Amantadine hydrochloride"
          },
          {
            "curie": "HMDB:HMDB0245807",
            "label": "Amantadine hydrochloride",
            "altLabel": "Hydrochloride, amantadine"
          },
          {
            "curie": "PUBCHEM.COMPOUND:2130",
            "label": "Amantadine hydrochloride",
            "altLabel": "Hydrochloride, amantadine"
          },
          {
            "curie": "PUBCHEM.COMPOUND:163285254",
            "label": "Amantadine-d15 Hydrochloride",
            "altLabel": None
          },
          {
            "curie": "UMLS:C2684460",
            "label": "amantadine hydrochloride 100 MG",
            "altLabel": None
          },
          {
            "curie": "UMLS:C4720105",
            "label": "Amantadine Hydrochloride Tablets",
            "altLabel": None
          },
          {
            "curie": "UMLS:C2684458",
            "label": "amantadine hydrochloride 10 MG/ML",
            "altLabel": None
          },
          {
            "curie": "UMLS:C4720215",
            "label": "Amantadine Hydrochloride Capsules",
            "altLabel": None
          }
        ],
        "id_curie": "UMLS:C0936072",
        "id_label": "Amantadine Hydrochloride",
        "id_uri": "http://identifiers.org/umls/C0936072"
      },
      "p": {
        "id": "https://w3id.org/biolink/vocab/treats",
        "curie": "biolink:treats",
        "label": "treats"
      },
      "o": {
        "index": "idiopathic Parkinson’s disease:1:68:98",
        "text": "idiopathic Parkinson’s disease",
        "type": "DiseaseOrPhenotypicFeature",
        "start": 68,
        "end": 98,
        "props": [],
        "curies": []
      }
    },
    {
      "s": {
        "index": "Amantadine hydrochloride:0:0:24",
        "text": "Amantadine hydrochloride",
        "type": "ChemicalEntity",
        "start": 0,
        "end": 24,
        "props": [],
        "curies": [
          {
            "curie": "UMLS:C0936072",
            "label": "Amantadine Hydrochloride",
            "altLabel": "AMANTADINE HYDROCHLORIDE"
          },
          {
            "curie": "PUBCHEM.COMPOUND:64150",
            "label": "Amantadine hydrochloride",
            "altLabel": None
          },
          {
            "curie": "PUBCHEM.COMPOUND:19031614",
            "label": "AMANTADINE HYDROCHLORIDE",
            "altLabel": "Amantadine hydrochloride"
          },
          {
            "curie": "HMDB:HMDB0245807",
            "label": "Amantadine hydrochloride",
            "altLabel": "Hydrochloride, amantadine"
          },
          {
            "curie": "PUBCHEM.COMPOUND:2130",
            "label": "Amantadine hydrochloride",
            "altLabel": "Hydrochloride, amantadine"
          },
          {
            "curie": "PUBCHEM.COMPOUND:163285254",
            "label": "Amantadine-d15 Hydrochloride",
            "altLabel": None
          },
          {
            "curie": "UMLS:C2684460",
            "label": "amantadine hydrochloride 100 MG",
            "altLabel": None
          },
          {
            "curie": "UMLS:C4720105",
            "label": "Amantadine Hydrochloride Tablets",
            "altLabel": None
          },
          {
            "curie": "UMLS:C2684458",
            "label": "amantadine hydrochloride 10 MG/ML",
            "altLabel": None
          },
          {
            "curie": "UMLS:C4720215",
            "label": "Amantadine Hydrochloride Capsules",
            "altLabel": None
          }
        ],
        "id_curie": "UMLS:C0936072",
        "id_label": "Amantadine Hydrochloride",
        "id_uri": "http://identifiers.org/umls/C0936072"
      },
      "p": {
        "id": "https://w3id.org/biolink/vocab/treats",
        "curie": "biolink:treats",
        "label": "treats"
      },
      "o": {
        "index": "postencephalitic parkinsonism:2:120:149",
        "text": "postencephalitic parkinsonism",
        "type": "DiseaseOrPhenotypicFeature",
        "start": 120,
        "end": 149,
        "props": [],
        "curies": [
          {
            "curie": "MONDO:0001945",
            "label": "postencephalitic Parkinsonism",
            "altLabel": "postencephalitic parkinsonism"
          }
        ],
        "id_curie": "MONDO:0001945",
        "id_label": "postencephalitic Parkinsonism",
        "id_uri": "http://purl.obolibrary.org/obo/MONDO_0001945"
      }
    },
    {
      "s": {
        "index": "Amantadine hydrochloride:0:0:24",
        "text": "Amantadine hydrochloride",
        "type": "ChemicalEntity",
        "start": 0,
        "end": 24,
        "props": [],
        "curies": [
          {
            "curie": "UMLS:C0936072",
            "label": "Amantadine Hydrochloride",
            "altLabel": "AMANTADINE HYDROCHLORIDE"
          },
          {
            "curie": "PUBCHEM.COMPOUND:64150",
            "label": "Amantadine hydrochloride",
            "altLabel": None
          },
          {
            "curie": "PUBCHEM.COMPOUND:19031614",
            "label": "AMANTADINE HYDROCHLORIDE",
            "altLabel": "Amantadine hydrochloride"
          },
          {
            "curie": "HMDB:HMDB0245807",
            "label": "Amantadine hydrochloride",
            "altLabel": "Hydrochloride, amantadine"
          },
          {
            "curie": "PUBCHEM.COMPOUND:2130",
            "label": "Amantadine hydrochloride",
            "altLabel": "Hydrochloride, amantadine"
          },
          {
            "curie": "PUBCHEM.COMPOUND:163285254",
            "label": "Amantadine-d15 Hydrochloride",
            "altLabel": None
          },
          {
            "curie": "UMLS:C2684460",
            "label": "amantadine hydrochloride 100 MG",
            "altLabel": None
          },
          {
            "curie": "UMLS:C4720105",
            "label": "Amantadine Hydrochloride Tablets",
            "altLabel": None
          },
          {
            "curie": "UMLS:C2684458",
            "label": "amantadine hydrochloride 10 MG/ML",
            "altLabel": None
          },
          {
            "curie": "UMLS:C4720215",
            "label": "Amantadine Hydrochloride Capsules",
            "altLabel": None
          }
        ],
        "id_curie": "UMLS:C0936072",
        "id_label": "Amantadine Hydrochloride",
        "id_uri": "http://identifiers.org/umls/C0936072"
      },
      "p": {
        "id": "https://w3id.org/biolink/vocab/treats",
        "curie": "biolink:treats",
        "label": "treats"
      },
      "o": {
        "index": "parkinsonism:3:166:178",
        "text": "parkinsonism",
        "type": "DiseaseOrPhenotypicFeature",
        "start": 166,
        "end": 178,
        "props": [],
        "curies": [
          {
            "curie": "DOID:0080855",
            "label": "Parkinsonism",
            "altLabel": "Parkinsonism"
          },
          {
            "curie": "MONDO:0021095",
            "label": "PARKINSONISM",
            "altLabel": "parkinsonism"
          },
          {
            "curie": "UMLS:C2939151",
            "label": "FH: Parkinsonism",
            "altLabel": "Family history: Parkinsonism"
          },
          {
            "curie": "MONDO:0009839",
            "label": "PSP-parkinsonism",
            "altLabel": "progressive supranuclear palsy-parkinsonism syndrome"
          },
          {
            "curie": "UMLS:C5548370",
            "label": "PSP-parkinsonism",
            "altLabel": "Progressive supranuclear palsy parkinsonism syndrome"
          },
          {
            "curie": "UMLS:C0752101",
            "label": "PARKINSONISM EXPER",
            "altLabel": "EXPER PARKINSONISM"
          },
          {
            "curie": "UMLS:C0270729",
            "label": "drugs; parkinsonism",
            "altLabel": "parkinsonism due to drug"
          },
          {
            "curie": "MONDO:0006966",
            "label": "PARKINSONISM SECOND",
            "altLabel": "SECOND PARKINSONISM"
          },
          {
            "curie": "UMLS:C1843796",
            "label": "Parkinsonism (later)",
            "altLabel": None
          },
          {
            "curie": "MONDO:0005180",
            "label": "Primary parkinsonism",
            "altLabel": "Primary Parkinsonism"
          }
        ],
        "id_curie": "DOID:0080855",
        "id_label": "Parkinsonism",
        "id_uri": "http://purl.obolibrary.org/obo/DOID_0080855"
      }
    },
    {
      "s": {
        "index": "Amantadine hydrochloride:0:0:24",
        "text": "Amantadine hydrochloride",
        "type": "ChemicalEntity",
        "start": 0,
        "end": 24,
        "props": [],
        "curies": [
          {
            "curie": "UMLS:C0936072",
            "label": "Amantadine Hydrochloride",
            "altLabel": "AMANTADINE HYDROCHLORIDE"
          },
          {
            "curie": "PUBCHEM.COMPOUND:64150",
            "label": "Amantadine hydrochloride",
            "altLabel": None
          },
          {
            "curie": "PUBCHEM.COMPOUND:19031614",
            "label": "AMANTADINE HYDROCHLORIDE",
            "altLabel": "Amantadine hydrochloride"
          },
          {
            "curie": "HMDB:HMDB0245807",
            "label": "Amantadine hydrochloride",
            "altLabel": "Hydrochloride, amantadine"
          },
          {
            "curie": "PUBCHEM.COMPOUND:2130",
            "label": "Amantadine hydrochloride",
            "altLabel": "Hydrochloride, amantadine"
          },
          {
            "curie": "PUBCHEM.COMPOUND:163285254",
            "label": "Amantadine-d15 Hydrochloride",
            "altLabel": None
          },
          {
            "curie": "UMLS:C2684460",
            "label": "amantadine hydrochloride 100 MG",
            "altLabel": None
          },
          {
            "curie": "UMLS:C4720105",
            "label": "Amantadine Hydrochloride Tablets",
            "altLabel": None
          },
          {
            "curie": "UMLS:C2684458",
            "label": "amantadine hydrochloride 10 MG/ML",
            "altLabel": None
          },
          {
            "curie": "UMLS:C4720215",
            "label": "Amantadine Hydrochloride Capsules",
            "altLabel": None
          }
        ],
        "id_curie": "UMLS:C0936072",
        "id_label": "Amantadine Hydrochloride",
        "id_uri": "http://identifiers.org/umls/C0936072"
      },
      "p": {
        "id": "https://w3id.org/biolink/vocab/treats",
        "curie": "biolink:treats",
        "label": "treats"
      },
      "o": {
        "index": "injury to the nervous system:4:196:224",
        "text": "injury to the nervous system",
        "type": "DiseaseOrPhenotypicFeature",
        "start": 196,
        "end": 224,
        "props": [],
        "curies": []
      }
    },
    {
      "s": {
        "index": "Amantadine hydrochloride:0:0:24",
        "text": "Amantadine hydrochloride",
        "type": "ChemicalEntity",
        "start": 0,
        "end": 24,
        "props": [],
        "curies": [
          {
            "curie": "UMLS:C0936072",
            "label": "Amantadine Hydrochloride",
            "altLabel": "AMANTADINE HYDROCHLORIDE"
          },
          {
            "curie": "PUBCHEM.COMPOUND:64150",
            "label": "Amantadine hydrochloride",
            "altLabel": None
          },
          {
            "curie": "PUBCHEM.COMPOUND:19031614",
            "label": "AMANTADINE HYDROCHLORIDE",
            "altLabel": "Amantadine hydrochloride"
          },
          {
            "curie": "HMDB:HMDB0245807",
            "label": "Amantadine hydrochloride",
            "altLabel": "Hydrochloride, amantadine"
          },
          {
            "curie": "PUBCHEM.COMPOUND:2130",
            "label": "Amantadine hydrochloride",
            "altLabel": "Hydrochloride, amantadine"
          },
          {
            "curie": "PUBCHEM.COMPOUND:163285254",
            "label": "Amantadine-d15 Hydrochloride",
            "altLabel": None
          },
          {
            "curie": "UMLS:C2684460",
            "label": "amantadine hydrochloride 100 MG",
            "altLabel": None
          },
          {
            "curie": "UMLS:C4720105",
            "label": "Amantadine Hydrochloride Tablets",
            "altLabel": None
          },
          {
            "curie": "UMLS:C2684458",
            "label": "amantadine hydrochloride 10 MG/ML",
            "altLabel": None
          },
          {
            "curie": "UMLS:C4720215",
            "label": "Amantadine Hydrochloride Capsules",
            "altLabel": None
          }
        ],
        "id_curie": "UMLS:C0936072",
        "id_label": "Amantadine Hydrochloride",
        "id_uri": "http://identifiers.org/umls/C0936072"
      },
      "p": {
        "id": "https://w3id.org/biolink/vocab/treats",
        "curie": "biolink:treats",
        "label": "treats"
      },
      "o": {
        "index": "carbon monoxide:5:228:243",
        "text": "carbon monoxide",
        "type": "ChemicalEntity",
        "start": 228,
        "end": 243,
        "props": [],
        "curies": [
          {
            "curie": "PUBCHEM.COMPOUND:281",
            "label": "Carbon monoxide",
            "altLabel": "Carbon Monoxide"
          },
          {
            "curie": "UMLS:C0007018",
            "label": "Carbon monoxide",
            "altLabel": "Carbon Monoxide"
          },
          {
            "curie": "UMLS:C4520712",
            "label": "Carbon monoxide",
            "altLabel": "Carbon monoxide measurement"
          },
          {
            "curie": "UMLS:C1268558",
            "label": "O15 Carbon Monoxide",
            "altLabel": "[15O]Carbon Monoxide"
          },
          {
            "curie": "UMLS:C1874024",
            "label": "AIR/CARBON MONOXIDE",
            "altLabel": None
          },
          {
            "curie": "PUBCHEM.COMPOUND:6432172",
            "label": "carbon monoxide(1+)",
            "altLabel": "CO(1+)"
          },
          {
            "curie": "UMLS:C1268564",
            "label": "Carbon Monoxide C-11",
            "altLabel": "Carbon Monoxide, C-11"
          },
          {
            "curie": "UMLS:C0007020",
            "label": "CARBON MONOXIDE POIS",
            "altLabel": "POIS CARBON MONOXIDE"
          },
          {
            "curie": "PUBCHEM.COMPOUND:10313038",
            "label": "CARBON MONOXIDE C-11",
            "altLabel": "Carbon monoxide c-11"
          },
          {
            "curie": "PUBCHEM.COMPOUND:10129878",
            "label": "CARBON MONOXIDE, O-15",
            "altLabel": "Carbon monoxide, O-15"
          }
        ],
        "id_curie": "PUBCHEM.COMPOUND:281",
        "id_label": "Carbon monoxide",
        "id_uri": "http://identifiers.org/pubchem.compound/281"
      }
    },
    {
      "s": {
        "index": "idiopathic Parkinson’s disease:1:68:98",
        "text": "idiopathic Parkinson’s disease",
        "type": "DiseaseOrPhenotypicFeature",
        "start": 68,
        "end": 98,
        "props": [],
        "curies": []
      },
      "p": {
        "id": "https://w3id.org/biolink/vocab/associated_with",
        "curie": "biolink:associated_with",
        "label": "associated with"
      },
      "o": {
        "index": "carbon monoxide:5:228:243",
        "text": "carbon monoxide",
        "type": "ChemicalEntity",
        "start": 228,
        "end": 243,
        "props": [],
        "curies": [
          {
            "curie": "PUBCHEM.COMPOUND:281",
            "label": "Carbon monoxide",
            "altLabel": "Carbon Monoxide"
          },
          {
            "curie": "UMLS:C0007018",
            "label": "Carbon monoxide",
            "altLabel": "Carbon Monoxide"
          },
          {
            "curie": "UMLS:C4520712",
            "label": "Carbon monoxide",
            "altLabel": "Carbon monoxide measurement"
          },
          {
            "curie": "UMLS:C1268558",
            "label": "O15 Carbon Monoxide",
            "altLabel": "[15O]Carbon Monoxide"
          },
          {
            "curie": "UMLS:C1874024",
            "label": "AIR/CARBON MONOXIDE",
            "altLabel": None
          },
          {
            "curie": "PUBCHEM.COMPOUND:6432172",
            "label": "carbon monoxide(1+)",
            "altLabel": "CO(1+)"
          },
          {
            "curie": "UMLS:C1268564",
            "label": "Carbon Monoxide C-11",
            "altLabel": "Carbon Monoxide, C-11"
          },
          {
            "curie": "UMLS:C0007020",
            "label": "CARBON MONOXIDE POIS",
            "altLabel": "POIS CARBON MONOXIDE"
          },
          {
            "curie": "PUBCHEM.COMPOUND:10313038",
            "label": "CARBON MONOXIDE C-11",
            "altLabel": "Carbon monoxide c-11"
          },
          {
            "curie": "PUBCHEM.COMPOUND:10129878",
            "label": "CARBON MONOXIDE, O-15",
            "altLabel": "Carbon monoxide, O-15"
          }
        ],
        "id_curie": "PUBCHEM.COMPOUND:281",
        "id_label": "Carbon monoxide",
        "id_uri": "http://identifiers.org/pubchem.compound/281"
      }
    },
    {
      "s": {
        "index": "postencephalitic parkinsonism:2:120:149",
        "text": "postencephalitic parkinsonism",
        "type": "DiseaseOrPhenotypicFeature",
        "start": 120,
        "end": 149,
        "props": [],
        "curies": [
          {
            "curie": "MONDO:0001945",
            "label": "postencephalitic Parkinsonism",
            "altLabel": "postencephalitic parkinsonism"
          }
        ],
        "id_curie": "MONDO:0001945",
        "id_label": "postencephalitic Parkinsonism",
        "id_uri": "http://purl.obolibrary.org/obo/MONDO_0001945"
      },
      "p": {
        "id": "https://w3id.org/biolink/vocab/positively_correlated_with",
        "curie": "biolink:positively_correlated_with",
        "label": "positively correlated with"
      },
      "o": {
        "index": "carbon monoxide:5:228:243",
        "text": "carbon monoxide",
        "type": "ChemicalEntity",
        "start": 228,
        "end": 243,
        "props": [],
        "curies": [
          {
            "curie": "PUBCHEM.COMPOUND:281",
            "label": "Carbon monoxide",
            "altLabel": "Carbon Monoxide"
          },
          {
            "curie": "UMLS:C0007018",
            "label": "Carbon monoxide",
            "altLabel": "Carbon Monoxide"
          },
          {
            "curie": "UMLS:C4520712",
            "label": "Carbon monoxide",
            "altLabel": "Carbon monoxide measurement"
          },
          {
            "curie": "UMLS:C1268558",
            "label": "O15 Carbon Monoxide",
            "altLabel": "[15O]Carbon Monoxide"
          },
          {
            "curie": "UMLS:C1874024",
            "label": "AIR/CARBON MONOXIDE",
            "altLabel": None
          },
          {
            "curie": "PUBCHEM.COMPOUND:6432172",
            "label": "carbon monoxide(1+)",
            "altLabel": "CO(1+)"
          },
          {
            "curie": "UMLS:C1268564",
            "label": "Carbon Monoxide C-11",
            "altLabel": "Carbon Monoxide, C-11"
          },
          {
            "curie": "UMLS:C0007020",
            "label": "CARBON MONOXIDE POIS",
            "altLabel": "POIS CARBON MONOXIDE"
          },
          {
            "curie": "PUBCHEM.COMPOUND:10313038",
            "label": "CARBON MONOXIDE C-11",
            "altLabel": "Carbon monoxide c-11"
          },
          {
            "curie": "PUBCHEM.COMPOUND:10129878",
            "label": "CARBON MONOXIDE, O-15",
            "altLabel": "Carbon monoxide, O-15"
          }
        ],
        "id_curie": "PUBCHEM.COMPOUND:281",
        "id_label": "Carbon monoxide",
        "id_uri": "http://identifiers.org/pubchem.compound/281"
      }
    },
    {
      "s": {
        "index": "parkinsonism:3:166:178",
        "text": "parkinsonism",
        "type": "DiseaseOrPhenotypicFeature",
        "start": 166,
        "end": 178,
        "props": [],
        "curies": [
          {
            "curie": "DOID:0080855",
            "label": "Parkinsonism",
            "altLabel": "Parkinsonism"
          },
          {
            "curie": "MONDO:0021095",
            "label": "PARKINSONISM",
            "altLabel": "parkinsonism"
          },
          {
            "curie": "UMLS:C2939151",
            "label": "FH: Parkinsonism",
            "altLabel": "Family history: Parkinsonism"
          },
          {
            "curie": "MONDO:0009839",
            "label": "PSP-parkinsonism",
            "altLabel": "progressive supranuclear palsy-parkinsonism syndrome"
          },
          {
            "curie": "UMLS:C5548370",
            "label": "PSP-parkinsonism",
            "altLabel": "Progressive supranuclear palsy parkinsonism syndrome"
          },
          {
            "curie": "UMLS:C0752101",
            "label": "PARKINSONISM EXPER",
            "altLabel": "EXPER PARKINSONISM"
          },
          {
            "curie": "UMLS:C0270729",
            "label": "drugs; parkinsonism",
            "altLabel": "parkinsonism due to drug"
          },
          {
            "curie": "MONDO:0006966",
            "label": "PARKINSONISM SECOND",
            "altLabel": "SECOND PARKINSONISM"
          },
          {
            "curie": "UMLS:C1843796",
            "label": "Parkinsonism (later)",
            "altLabel": None
          },
          {
            "curie": "MONDO:0005180",
            "label": "Primary parkinsonism",
            "altLabel": "Primary Parkinsonism"
          }
        ],
        "id_curie": "DOID:0080855",
        "id_label": "Parkinsonism",
        "id_uri": "http://purl.obolibrary.org/obo/DOID_0080855"
      },
      "p": {
        "id": "https://w3id.org/biolink/vocab/positively_correlated_with",
        "curie": "biolink:positively_correlated_with",
        "label": "positively correlated with"
      },
      "o": {
        "index": "carbon monoxide:5:228:243",
        "text": "carbon monoxide",
        "type": "ChemicalEntity",
        "start": 228,
        "end": 243,
        "props": [],
        "curies": [
          {
            "curie": "PUBCHEM.COMPOUND:281",
            "label": "Carbon monoxide",
            "altLabel": "Carbon Monoxide"
          },
          {
            "curie": "UMLS:C0007018",
            "label": "Carbon monoxide",
            "altLabel": "Carbon Monoxide"
          },
          {
            "curie": "UMLS:C4520712",
            "label": "Carbon monoxide",
            "altLabel": "Carbon monoxide measurement"
          },
          {
            "curie": "UMLS:C1268558",
            "label": "O15 Carbon Monoxide",
            "altLabel": "[15O]Carbon Monoxide"
          },
          {
            "curie": "UMLS:C1874024",
            "label": "AIR/CARBON MONOXIDE",
            "altLabel": None
          },
          {
            "curie": "PUBCHEM.COMPOUND:6432172",
            "label": "carbon monoxide(1+)",
            "altLabel": "CO(1+)"
          },
          {
            "curie": "UMLS:C1268564",
            "label": "Carbon Monoxide C-11",
            "altLabel": "Carbon Monoxide, C-11"
          },
          {
            "curie": "UMLS:C0007020",
            "label": "CARBON MONOXIDE POIS",
            "altLabel": "POIS CARBON MONOXIDE"
          },
          {
            "curie": "PUBCHEM.COMPOUND:10313038",
            "label": "CARBON MONOXIDE C-11",
            "altLabel": "Carbon monoxide c-11"
          },
          {
            "curie": "PUBCHEM.COMPOUND:10129878",
            "label": "CARBON MONOXIDE, O-15",
            "altLabel": "Carbon monoxide, O-15"
          }
        ],
        "id_curie": "PUBCHEM.COMPOUND:281",
        "id_label": "Carbon monoxide",
        "id_uri": "http://identifiers.org/pubchem.compound/281"
      }
    },
    {
      "s": {
        "index": "injury to the nervous system:4:196:224",
        "text": "injury to the nervous system",
        "type": "DiseaseOrPhenotypicFeature",
        "start": 196,
        "end": 224,
        "props": [],
        "curies": []
      },
      "p": {
        "id": "https://w3id.org/biolink/vocab/positively_correlated_with",
        "curie": "biolink:positively_correlated_with",
        "label": "positively correlated with"
      },
      "o": {
        "index": "carbon monoxide:5:228:243",
        "text": "carbon monoxide",
        "type": "ChemicalEntity",
        "start": 228,
        "end": 243,
        "props": [],
        "curies": [
          {
            "curie": "PUBCHEM.COMPOUND:281",
            "label": "Carbon monoxide",
            "altLabel": "Carbon Monoxide"
          },
          {
            "curie": "UMLS:C0007018",
            "label": "Carbon monoxide",
            "altLabel": "Carbon Monoxide"
          },
          {
            "curie": "UMLS:C4520712",
            "label": "Carbon monoxide",
            "altLabel": "Carbon monoxide measurement"
          },
          {
            "curie": "UMLS:C1268558",
            "label": "O15 Carbon Monoxide",
            "altLabel": "[15O]Carbon Monoxide"
          },
          {
            "curie": "UMLS:C1874024",
            "label": "AIR/CARBON MONOXIDE",
            "altLabel": None
          },
          {
            "curie": "PUBCHEM.COMPOUND:6432172",
            "label": "carbon monoxide(1+)",
            "altLabel": "CO(1+)"
          },
          {
            "curie": "UMLS:C1268564",
            "label": "Carbon Monoxide C-11",
            "altLabel": "Carbon Monoxide, C-11"
          },
          {
            "curie": "UMLS:C0007020",
            "label": "CARBON MONOXIDE POIS",
            "altLabel": "POIS CARBON MONOXIDE"
          },
          {
            "curie": "PUBCHEM.COMPOUND:10313038",
            "label": "CARBON MONOXIDE C-11",
            "altLabel": "Carbon monoxide c-11"
          },
          {
            "curie": "PUBCHEM.COMPOUND:10129878",
            "label": "CARBON MONOXIDE, O-15",
            "altLabel": "Carbon monoxide, O-15"
          }
        ],
        "id_curie": "PUBCHEM.COMPOUND:281",
        "id_label": "Carbon monoxide",
        "id_uri": "http://identifiers.org/pubchem.compound/281"
      }
    }
  ]
}