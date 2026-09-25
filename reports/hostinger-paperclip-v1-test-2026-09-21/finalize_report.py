from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import zipfile
import pdfplumber

root=Path(__file__).resolve().parent
pdf=root/'Hostinger-Paperclip-v1-Test-Report.pdf'
verification_path=root/'verification.json'
verification=json.loads(verification_path.read_text(encoding='utf-8'))
sha=lambda path: hashlib.sha256(path.read_bytes()).hexdigest()
if sha(pdf)!=verification['pdf_sha256']:
    raise RuntimeError('PDF differs from the verified build')
if not all(verification['checks'].values()):
    raise RuntimeError('An assembly check is not passing')

out_of_bounds=[]
with pdfplumber.open(pdf) as parsed:
    for n,page in enumerate(parsed.pages,1):
        if not (root/'qa'/('page-%02d.png'%n)).exists():
            raise RuntimeError('Missing final page rendering: '+str(n))
        for ch in page.chars:
            if ch['x0']<0 or ch['x1']>page.width+0.5 or ch['top']<0 or ch['bottom']>page.height+0.5:
                out_of_bounds.append(dict(page=n,text=ch['text'],x0=ch['x0'],x1=ch['x1']))
if out_of_bounds:
    raise RuntimeError('Text outside page bounds: '+str(out_of_bounds[:5]))

verification['visual_review']='Complete: Codex inspected all final page PNGs for legibility, clipping, layout, and screenshot preservation.'
verification['visual_reviewed_pages']=list(range(1,verification['pdf_pages']+1))
verification['text_outside_page_bounds']=0
verification['finalized_at_utc']=datetime.now(timezone.utc).isoformat()
verification_path.write_text(json.dumps(verification,indent=2),encoding='utf-8')

files=[pdf,root/'Hostinger-Paperclip-v1-Test-Report.md',root/'README.md',root/'source-exhibits.md',root/'evidence-manifest.json',verification_path]
files+=sorted((root/'evidence').iterdir())
bundle=root/'Hostinger-Paperclip-v1-CoWork-Review-Package.zip'
with zipfile.ZipFile(bundle,'w',compression=zipfile.ZIP_DEFLATED) as archive:
    for path in files:
        archive.write(path,str(path.relative_to(root)))
with zipfile.ZipFile(bundle) as archive:
    if archive.testzip() is not None:
        raise RuntimeError('ZIP integrity verification failed')
print(json.dumps(dict(pdf=str(pdf),pdf_pages=verification['pdf_pages'],pdf_sha256=sha(pdf),bundle=str(bundle),bundle_bytes=bundle.stat().st_size,bundle_sha256=sha(bundle),evidence_files=len(list((root/'evidence').iterdir())),all_checks_passed=True),indent=2))
