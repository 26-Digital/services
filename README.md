# Services
26Digitalbw services DX API 
# services
Created Setswana Natural language processing tool REST API to service a NEXTJS website

## Troubleshooting links
1. https://stackoverflow.com/questions/23439089/using-django-admin-on-windows-powershell
2. https://parmarnaitik0909.medium.com/deploying-hosting-a-django-website-on-cpanel-with-git-version-control-6e8dce70a316

## Useful links
1. https://tailwindcss.com/docs/aspect-ratio

## JSON Serialization
1. USE json.dumps() TO CONVERT DATA TO A STRING OF A JSON OBJECT AND json.loads() TO CREATE A JSON OBJECT.
2. https://www.adamsmith.haus/python/answers/how-to-create-a-json-object-in-python

## Lerui-Compound-Natural Language Processing
 @author: Bopaki Tebalo  
 Chunks: 
    'lerui' in a sentence. 
    'letlhaodi' in a sentence. 
    'lebadi' in a sentence.         
    'leemedi' in a sentence.         
    'leamanyi' in a sentence.         
    'lesupi' in a sentence.         
    'letlhalosi' in a sentence. 
 Dikarolo tsa puo:     
    leina(noun)     
    leemedi(pronoun)     
    lediri(verb)     
    ditlhaodi(qualificatives):         
    lesupi(demostrative) e.g  Go nole kgomo ele fela-'ele' ke lesupi(a mangwe ke bo 'e' 'eo') o othe a supa gore selo se go buiwang ka sone          
    lebadi(enumerative)  e.g  Go nole kgomo ele nngwefela-'nngwe' ke lebadi         
    letlhaodi(adjective) e.g Monna yo moleele o lobelo.


# Current issues
1. We cant repeat keys on a dictionary, therefore some keys are omitted.
   Example:
   Input:
      (S
         (NN-T Monna/NN 
            (leamanyi
               yo/CC1 
               o/CC4 
               lemang/VRB_ng)
            )
         o/CC4
         itse/VRB
         botshelo/NN
      ./.)

   Output:
      {
         "S": {
            "NN-T": {
                  "NN": "Monna",
                  "leamanyi": {
                     "CC1": "yo",
                     "CC4": "o",
                     "VRB_ng": "lemang",
                     "VRB": "itse",
                     "NN": "botshelo",
                     ".": "."
                  }
            }
         }
      }
   Desired Output:
      {
         "S": {
            "NN-T": {
                  "NN": "Monna",
                  "leamanyi": {
                     "CC1": "yo",
                     "CC4": "o",
                     "VRB_ng": "lemang",
                      }
                }
            "CC4": "o",
            "VRB": "itse",
            "NN": "botshelo",
            ".": "."
         }
      }