from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class FreqWordsForm(FlaskForm):
    dna_seq = TextAreaField('DNA Sequence', validators=[DataRequired()])
    k_val = TextAreaField('K value of K-mer',validators=[DataRequired()])
    submit = SubmitField('Calculate')

class ReverseComplementForm(FlaskForm):
    dna_seq = TextAreaField('DNA Sequence', validators=[DataRequired()])
    submit = SubmitField('Calculate')

class PatternMatchingForm(FlaskForm):
    dna_seq = TextAreaField('Genome', validators=[DataRequired()])
    pattern = TextAreaField('Pattern to match',validators=[DataRequired()])
    submit = SubmitField('Calculate')

class PatternCountForm(FlaskForm):
    dna_seq = TextAreaField('Genome', validators=[DataRequired()])
    pattern = TextAreaField('Pattern to count',validators=[DataRequired()])
    submit = SubmitField('Calculate')


class HammingDistanceForm(FlaskForm):
    pattern_p = TextAreaField('Sequence P', validators=[DataRequired()])
    pattern_q = TextAreaField('Sequence Q',validators=[DataRequired()])
    submit = SubmitField('Calculate')

class FreqWordsWithMismatchForm(FlaskForm):
	dna_seq = TextAreaField('DNA Sequence', validators=[DataRequired()])
	distance = IntegerField('How many mismatches', validators=[DataRequired()])
	k_val = IntegerField('K value of K-mer',validators=[DataRequired()])
	submit = SubmitField('Calculate')

