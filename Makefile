.PHONY: resume watch clean

resume: resume_pdf resume_html

watch:
	ls *.md *.css | entr make resume

resume_html: resume.md resume.py
	. ./venv/bin/activate;\
	python resume.py resume.md resume.html resume.css

resume_pdf: resume_html resume.css
	. ./venv/bin/activate;\
	weasyprint resume.html resume.pdf -s resume.css --presentational-hints;\
	deactivate
clean:
	rm -f resume.html resume.pdf
