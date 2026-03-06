from fpdf import FPDF


def generate_pdf(itinerary, start_date, days):

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", "B", 18)
    pdf.cell(0, 10, "GlobeTrek AI Travel Plan", ln=True)

    pdf.ln(5)

    pdf.set_font("Arial", "", 12)

    pdf.cell(0, 8, f"Start Date: {start_date}", ln=True)
    pdf.cell(0, 8, f"Trip Duration: {days} days", ln=True)

    pdf.ln(10)

    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 8, "Daily Itinerary", ln=True)

    pdf.ln(5)

    pdf.set_font("Arial", "", 12)

    for day in itinerary:

        line = f"{day['date']} - {day['destination']}"

        # remove characters not supported by latin-1
        line = line.encode("latin-1", "replace").decode("latin-1")

        pdf.cell(0, 8, line, ln=True)

    file_path = "travel_itinerary.pdf"

    pdf.output(file_path)

    return file_path