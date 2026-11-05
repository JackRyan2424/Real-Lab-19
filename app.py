import streamlit as st

st.set_page_config(page_title="QQQ investor panel", layout="wide")
DATA={
"AAPL":{"company":"Apple Inc.","growth":"4.97%","lev":"2.61","checks":[("Buffett","ROE 15%+ every year","pass"),("Buffett","Owner earnings positive every year","pass"),("Buffett","Owner earnings grew first to last","pass"),("Cathie Wood","Revenue growth at least 15%","fail (4.97%)"),("Cathie Wood","R&D at least 5% latest year","pass (9.56%)"),("Burry","Operating cash flow at least net income every year","fail"),("Burry","Liabilities no more than twice equity","fail (2.61)")],"years":[("2022-09-24","394,328","26,251","6.66%","5.962"),("2023-09-30","383,285","29,915","7.80%","4.673"),("2024-09-28","391,035","31,370","8.02%","5.409"),("2025-09-27","416,161","34,550","8.30%","3.872"),("2026-09-26","478,834","45,765","9.56%","2.609")],"memos":{"Buffett":("own the business","ROE clears the hurdle every year, owner earnings stay positive and finish above their starting value. This supports a profitable business, but does not establish a durable moat, management quality or an attractive price."),"Cathie Wood":("pass","R&D is 9.56% of revenue, but revenue growth is 4.97%, below the 15% high-growth hurdle. R&D spending alone cannot prove disruptive innovation or future market expansion."),"Burry":("pass","Operating cash flow falls below net income in a selected year, and liabilities/equity is 2.61, above the ceiling of 2. These are research flags, not proof of manipulation or insolvency.")}},
"COST":{"company":"COSTCO WHOLESALE CORP /NEW","growth":"7.51%","lev":"1.49","checks":[("Buffett","ROE 15%+ every year","pass"),("Buffett","Owner earnings positive every year","pass"),("Buffett","Owner earnings grew first to last","pass"),("Cathie Wood","Revenue growth at least 15%","fail (7.51%)"),("Cathie Wood","R&D at least 5% latest year","not known"),("Burry","Operating cash flow at least net income every year","pass"),("Burry","Liabilities no more than twice equity","pass (1.49)")],"years":[("2022-08-28","226,954","not found","not known","2.108"),("2023-09-03","242,290","not found","not known","1.753"),("2024-09-01","254,453","not found","not known","1.956"),("2025-08-31","275,235","not found","not known","1.644"),("2026-08-30","303,154","not found","not known","1.487")],"memos":{"Buffett":("own the business","ROE clears the hurdle every year, owner earnings are positive and rise from 3,501 million to 9,382 million USD. The cash evidence supports the case, but does not establish moat, management quality or price."),"Cathie Wood":("pass","Revenue growth of 7.51% is below the 15% hurdle. R&D is not found, so that check remains not known; missing disclosure is not evidence of no innovation."),"Burry":("watch it","Operating cash flow covers net income every selected year and liabilities/equity is 1.49, below 2. These checks support further research, not a complete conclusion.")}}
}

st.title("QQQ investor skill app")
st.markdown("**Fund:** Invesco QQQ · **Selected company:** Apple (AAPL)")
st.caption("Apple is QQQ's largest holding on Invesco's November 3, 2026 holdings list (8.13%).")
choice=st.segmented_control("Company",["AAPL","COST"],default="AAPL") or "AAPL"
d=DATA[choice]
st.subheader(d["company"])
st.caption("Saved SEC snapshot; printed values only. Missing values remain not known or not found.")
st.write(f"Revenue growth a year: **{d['growth']}** · Latest liabilities/equity: **{d['lev']}**")
st.table([{"Investor":a,"Check":b,choice:c} for a,b,c in d["checks"]])
st.subheader("Annual evidence")
st.table([{"Fiscal year end":a,"Revenue (USD millions)":b,"R&D (USD millions)":c,"R&D / revenue":e,"Liabilities / equity":f} for a,b,c,e,f in d["years"]])
st.subheader("Three FAskills-format investor memos")
for col,investor in zip(st.columns(3),("Buffett","Cathie Wood","Burry")):
    verdict,memo=d["memos"][investor]
    with col:
        st.markdown(f"### {investor}")
        st.markdown(f"**Verdict:** {verdict}")
        st.caption("AI simulation; not an authentic investor statement. Forecasts, prices, scores and actual holdings are not known from this classroom data.")
        st.write(memo)
        st.markdown("**Forward outlook:** not known; this screen does not forecast.\n\n**Key risks:** preserve unknowns and investigate failed checks.\n\n**What changes my mind:** new filing evidence explaining the gap.")
st.subheader("Threshold probe")
st.write("COST's growth check changes from fail at 15% to pass at 5%; R&D stays not known. AAPL remains below 5%, so its growth check still fails.")
st.subheader("My decision")
st.write("I would trust the panel for initial screening, but only if missing data stay explicit and I review industry differences and valuation before investing.")
st.caption("Source formats: Warren Buffett, Cathie Wood and Michael Burry FAskills expert files. https://github.com/CinderZhang/FAskills/tree/main/financial-researcher/experts")
