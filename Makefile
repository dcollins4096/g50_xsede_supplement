
stuff = ms.tex

proposal:  $(stuff)
	pdflatex ms
	pdflatex ms
	bibtex ms
	pdflatex ms

o: $(stuff)
	pdflatex ms


scaling: Scaling.tex
	pdflatex Scaling
	pdflatex Scaling
	bibtex Scaling
	pdflatex Scaling
	pdflatex Scaling

progress: Progress.tex
	pdflatex Progress
	pdflatex Progress
	bibtex Progress
	pdflatex Progress
