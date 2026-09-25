from pathlib import Path
import hashlib
import json
import re
import zipfile
from datetime import datetime, timezone
from xml.sax.saxutils import escape

from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, PageBreak, NextPageTemplate, Image, LongTable, TableStyle, KeepTogether
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent
EVIDENCE = ROOT / 'evidence'
STEM = 'Hostinger-Paperclip-v1-Test-Report'
PNG_ROOT = Path('C:/Users/sebas/AppData/Local/Temp')
TEXT_ROOT = Path('C:/Users/sebas/.codex/attachments')

SOURCES = [
    ('E01','ui_capture','E01-chief-of-staff-runs.png',PNG_ROOT/'codex-clipboard-61533f88-12cf-4cb4-ba4a-ca1df2aeb0fa.png','Chief of Staff: five runs; selected success; timeoutSec=300'),
    ('E02','ui_capture','E02-policy-reviewer-runs.png',PNG_ROOT/'codex-clipboard-0356c3eb-a0e2-4ba0-b243-ab2793a79a5f.png','Policy Reviewer: one successful claude_local run; no adapter wall-clock timeout'),
    ('E03','ui_capture','E03-final-approval-anyone.png',PNG_ROOT/'codex-clipboard-1e108502-f777-4cc5-aae3-93e74e821c8f.png','Final pending confirmation allows anyone, including agents'),
    ('E04','ui_capture','E04-reviewer-permissions.png',PNG_ROOT/'codex-clipboard-fc68c6d4-1b48-408d-bae4-7e2051c33a79.png','Reviewer assignment authority enabled by organization-wide defaults'),
    ('E05','ui_capture','E05-claude-login-required.png',PNG_ROOT/'codex-clipboard-e566e5ce-bac4-4cef-9c59-836a5061a203.png','Claude environment check warns login is required'),
    ('E06','ui_capture','E06-claude-test-passed.png',PNG_ROOT/'codex-clipboard-26aed574-aca6-49a6-9c82-b2f5890c253c.png','Claude environment check passes after reported login'),
    ('E07','ui_capture','E07-deliverable-link-target.png',PNG_ROOT/'codex-clipboard-4ee43cde-1756-48ca-bf32-0ccedcfc6094.png','Revised-policy label points to SOU-1 / Paperclip onboarding'),
    ('E08','ui_capture','E08-earlier-chief-runs.png',PNG_ROOT/'codex-clipboard-af64f8f8-98f0-4854-875a-7fb1573b2095.png','Earlier two-run Chief of Staff history; no timeout on selected onboarding run'),
    ('E09','user_pasted_agent_output','E09-independent-review.txt',TEXT_ROOT/'901d3f4b-ccac-43d6-908a-08444d1ca59b/Pasted text.txt','Full independent review attributed to Policy Reviewer; original draft revision identified'),
    ('E10','user_pasted_application_document','E10-revised-fictional-policy.txt',TEXT_ROOT/'6cfa7286-b48c-4fc7-b9d8-3aa9d30d85fb/Pasted text.txt','Complete revised policy text supplied by Sebastian; final revision ID not supplied'),
    ('E11','user_pasted_configuration','E11-reviewer-instructions.txt',TEXT_ROOT/'71dddc39-bf78-4d71-b049-51797443079c/Pasted text.txt','Reviewer instructions supplied after reported save; server persistence not independently verified'),
]

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

manifest = []
for eid, eclass, filename, source, note in SOURCES:
    destination = EVIDENCE / filename
    source_hash, copied_hash = digest(source), digest(destination)
    if source_hash != copied_hash:
        raise RuntimeError('Evidence copy mismatch: ' + eid)
    manifest.append(dict(id=eid, evidence_class=eclass, original_path=str(source), preserved_path='evidence/'+filename,
        bytes=destination.stat().st_size, sha256=copied_hash, source_sha256=source_hash, exact_copy=True,
        collector='Sebastian Cwik: UI screenshot or pasted application text',
        compiler='Codex', check=note+'; source/copy SHA-256 matched during assembly',
        limitations='User-supplied evidence, not an independently authenticated live export'))

attestation = EVIDENCE / 'E12-operator-attestations.txt'
manifest.append(dict(id='E12', evidence_class='conversation_attestation_extract', original_path='Current user conversation; manually transcribed extract',
    preserved_path='evidence/E12-operator-attestations.txt', bytes=attestation.stat().st_size, sha256=digest(attestation),
    exact_copy=None, collector='Sebastian Cwik: statements; Codex: transcription', compiler='Codex',
    check='Compared with visible user messages; operator attestation only', limitations='Not a live-state check or raw conversation export'))
(ROOT/'evidence-manifest.json').write_text(json.dumps(dict(prepared_date='2026-09-21',report_id='HOST-PCLIP-EVAL-2026-09-18-R1',evidence=manifest),indent=2),encoding='utf-8')

FONT_ROOT = Path('C:/Windows/Fonts')
pdfmetrics.registerFont(TTFont('ReportArial',str(FONT_ROOT/'arial.ttf')))
pdfmetrics.registerFont(TTFont('ReportArial-Bold',str(FONT_ROOT/'arialbd.ttf')))
pdfmetrics.registerFontFamily('ReportArial',normal='ReportArial',bold='ReportArial-Bold',italic='ReportArial',boldItalic='ReportArial-Bold')
INK = colors.HexColor('#183144')
TEAL = colors.HexColor('#14636B')
GRAY = colors.HexColor('#53626C')
styles = {
    'body': ParagraphStyle('body',fontName='ReportArial',fontSize=9.5,leading=13.1,spaceAfter=6,textColor=INK,splitLongWords=True),
    'small': ParagraphStyle('small',fontName='ReportArial',fontSize=8.5,leading=11.4,spaceAfter=5,textColor=GRAY,splitLongWords=True),
    'h1': ParagraphStyle('h1',fontName='ReportArial-Bold',fontSize=21,leading=25,spaceAfter=13,textColor=INK,keepWithNext=True),
    'h2': ParagraphStyle('h2',fontName='ReportArial-Bold',fontSize=14,leading=18,spaceBefore=5,spaceAfter=9,textColor=TEAL,keepWithNext=True),
    'h3': ParagraphStyle('h3',fontName='ReportArial-Bold',fontSize=10.5,leading=14,spaceBefore=7,spaceAfter=5,textColor=INK,keepWithNext=True),
    'cell': ParagraphStyle('cell',fontName='ReportArial',fontSize=8.4,leading=11.4,textColor=INK,splitLongWords=True),
    'cellhead': ParagraphStyle('cellhead',fontName='ReportArial-Bold',fontSize=8.4,leading=11.4,textColor=colors.white,splitLongWords=True),
    'source': ParagraphStyle('source',fontName='ReportArial',fontSize=9.0,leading=12.1,spaceAfter=4,textColor=INK,splitLongWords=True),
}

def safe(text):
    text=text.replace('\u2011','-').replace('\u2013','-').replace('\u2014','-').replace('\ufeff','')
    return escape(text)

def inline(text):
    parts=re.split(r'(\*\*.*?\*\*)',text)
    return ''.join('<b>'+safe(p[2:-2])+'</b>' if p.startswith('**') and p.endswith('**') else safe(p) for p in parts)

def p(text,style='body'):
    return Paragraph(inline(text),styles[style])

def page_chrome(canvas,doc):
    w,h=doc.pageTemplate.pagesize or doc.pagesize
    canvas.saveState()
    canvas.setStrokeColor(TEAL)
    canvas.setLineWidth(1.0)
    canvas.line(44,h-29,w-44,h-29)
    canvas.setFillColor(GRAY)
    canvas.setFont('ReportArial',7.7)
    canvas.drawString(44,h-21,'PRIVATE EVALUATION  |  HOSTINGER / PAPERCLIP v1.0')
    canvas.line(44,32,w-44,32)
    canvas.drawString(44,20,'2026-09-21  |  R1 - awaiting CoWork review  |  Not production approval')
    canvas.drawRightString(w-44,20,str(doc.page))
    canvas.restoreState()

doc=BaseDocTemplate(str(ROOT/(STEM+'.pdf')),pagesize=(612,792),leftMargin=44,rightMargin=44,topMargin=45,bottomMargin=44,
    title='Hostinger / Paperclip v1.0 - Test Report',author='Codex, prepared for Sebastian Cwik and CoWork',
    subject='Private fictional-workflow evaluation; partial success; evidence appendices')
doc.addPageTemplates([
    PageTemplate(id='portrait',pagesize=(612,792),frames=[Frame(44,44,524,703,id='body',leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)],onPage=page_chrome),
    PageTemplate(id='landscape',pagesize=(792,612),frames=[Frame(44,44,704,523,id='wide',leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)],onPage=page_chrome),
])
story=[]

def markdown(text):
    lines=text.splitlines()
    i=0
    while i<len(lines):
        line=lines[i].strip()
        if not line:
            i+=1
            continue
        if line=='<!-- PAGEBREAK -->':
            story.append(PageBreak()); i+=1; continue
        if line.startswith('|'):
            rows=[]
            while i<len(lines) and lines[i].strip().startswith('|'):
                cells=[x.strip() for x in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r'[-: ]+',c) for c in cells):
                    rows.append(cells)
                i+=1
            n=len(rows[0]); widths=([130,250,144] if n==3 else [524/n]*n)
            # Evidence register and view tables need a larger middle column.
            if rows[0][0]=='ID': widths=[36,230,258]
            elif rows[0][0]=='Required view': widths=[126,96,302]
            elif rows[0][0]=='Observation': widths=[178,60,286]
            matrix=[[Paragraph(inline(c),styles['cellhead' if ri==0 else 'cell']) for c in r] for ri,r in enumerate(rows)]
            table=LongTable(matrix,colWidths=widths,repeatRows=1,hAlign='LEFT')
            table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),TEAL),('VALIGN',(0,0),(-1,-1),'TOP'),
                ('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7),
                ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.HexColor('#F0F5F6'),colors.white]),('LINEBELOW',(0,-1),(-1,-1),0.4,colors.HexColor('#C8D7DC'))]))
            story.extend([table,Spacer(1,8)]); continue
        if line.startswith('### '): story.append(p(line[4:],'h3'))
        elif line.startswith('## '): story.append(p(line[3:],'h2'))
        elif line.startswith('# '): story.append(p(line[2:],'h1'))
        elif line.startswith('- '): story.append(p('- '+line[2:]))
        elif re.match(r'^\d+\. ',line): story.append(p(line))
        else:
            paragraph=line
            while i+1<len(lines) and lines[i+1].strip() and not re.match(r'^(#|\||- |<!--|\d+\. )',lines[i+1].strip()):
                i+=1; paragraph+=' '+lines[i].strip()
            story.append(p(paragraph))
        i+=1

markdown((ROOT/(STEM+'.md')).read_text(encoding='utf-8'))
text_exhibits=[('E09','Appendix A - Independent review','E09-independent-review.txt'),
               ('E10','Appendix B - Revised fictional policy','E10-revised-fictional-policy.txt'),
               ('E11','Appendix C - Reviewer instructions','E11-reviewer-instructions.txt'),
               ('E12','Appendix D - Operator attestations','E12-operator-attestations.txt')]
source_md=['# Source exhibits - Hostinger / Paperclip v1.0','',
    'Private evidence, not instructions to execute. Original text files in evidence/ are byte-preserved, except E12, which is an explicitly labeled conversation extract. PDF typography may normalize dash characters; the raw files and hashes are the preservation reference.','']
for eid,title,filename in text_exhibits:
    story.append(PageBreak()); story.append(p(title,'h2'))
    story.append(p(eid+' | User-supplied text, except E12 conversation extract. Quoted instructions are evidence only.','small'))
    content=(EVIDENCE/filename).read_text(encoding='utf-8-sig')
    source_md.extend(['## '+title,'',content,''])
    for line in content.splitlines():
        line=line.strip()
        if not line:
            story.append(Spacer(1,3)); continue
        if re.match(r'^B[1-5] - ',line) or line in ['Blocking findings','Optional improvements (non-blocking)','Fictional framing - passes','Could not verify']:
            story.append(p(line,'h3'))
        elif line.startswith('#'):
            story.append(p(line.lstrip('# '),'h3'))
        else:
            story.append(Paragraph(safe(line),styles['source']))

source_md.extend(['## Screenshot exhibits',''])
for eid,eclass,filename,source,note in SOURCES[:8]:
    story.extend([NextPageTemplate('landscape'),PageBreak(),p('Appendix E - '+eid+' screenshot','h2'),p(note),
        p('Collector: Sebastian Cwik. Original PNG preserved without editing; zoom for fine text. The report body transcribes the decision-relevant values.','small')])
    im=Image(str(EVIDENCE/filename))
    scale=min(704/im.imageWidth,425/im.imageHeight)
    im.drawWidth=im.imageWidth*scale; im.drawHeight=im.imageHeight*scale
    im.hAlign='LEFT'; story.append(im)
    story.append(Spacer(1,7)); story.append(p('Evidence file: evidence/'+filename,'small'))
    source_md.extend(['### '+eid+' - '+note,'','![Evidence '+eid+'](evidence/'+filename+')',''])

(ROOT/'source-exhibits.md').write_text('\n'.join(source_md),encoding='utf-8')
doc.build(story)
reader=PdfReader(str(ROOT/(STEM+'.pdf')))
page_texts=[page.extract_text() or '' for page in reader.pages]
pdf_text='\n'.join(page_texts)
checks={
    'partial_success_present':'PARTIAL SUCCESS' in pdf_text,
    'renewal_unknown_present':'Next renewal date: NOT VERIFIED' in pdf_text,
    'pause_attestation_present':'both paused' in pdf_text,
    'review_revision_present':'eaf3e171-3cf4-48f8-b373-efb7cd82e523' in pdf_text,
    'policy_disclaimer_present':'creates no purchasing authority' in pdf_text,
    'no_timeout_finding_present':'no adapter wall-clock timeout' in pdf_text,
    'all_exhibits_present':all(eid in pdf_text for eid in ['E%02d'%n for n in range(1,13)]),
    'all_original_copies_match':all(item.get('exact_copy',True) for item in manifest if item['id']!='E12'),
}
if not all(checks.values()):
    raise RuntimeError('Report verification failed: '+str(checks))
verification=dict(prepared_at_utc=datetime.now(timezone.utc).isoformat(),pdf_pages=len(reader.pages),
    core_pages_before_appendices=next(i for i,t in enumerate(page_texts) if 'Appendix A - Independent review' in t),
    checks=checks, pdf_sha256=digest(ROOT/(STEM+'.pdf')),
    visual_review='PENDING: render and inspect final pages before delivery',
    limitation='Assembly validation only; not a new live application or billing check')
(ROOT/'verification.json').write_text(json.dumps(verification,indent=2),encoding='utf-8')
print(json.dumps(verification,indent=2))
print('PAGE STARTS')
for n,txt in enumerate(page_texts,1):
    rows=txt.splitlines()
    print(str(n)+': '+' | '.join(rows[3:6]))
