

plan_details = {'tds':300, 'deductible':400, 'initcovlimit': 3700, 'trooplimit':4950, 'ccl':7425}



def OOPCalc(plan_details):
    OOP = 0
    status = None
    medcov = 0
    gap = 0
    ICL = 0
    pdd = plan_details['deductible']
    tds = plan_details['tds']
    if tds <= pdd:
        OOP = tds
        status = 'Deductible'
    else:
        # the total drug spend has exceeded the deductible. 25% of incremental costs are now out of pocket
        # adding to OOP costs until OOP reaches $3,700
        if tds <= plan_details['initcovlimit']:
            status = 'Initial Coverage'
            ICL = ((tds - pdd) * .25)
            medcov = ((tds - pdd) * .75)
            OOP = ICL + pdd
        if tds > plan_details['initcovlimit'] and tds <= plan_details['ccl']:
            # the total drug spend has reached the donut hole, exceeding $3,700 and less than $7,425.
            status = 'Donut Hole'
            gap = tds - plan_details['initcovlimit']
            ICL = (plan_details['initcovlimit'] - pdd) * .25
            medcov = (plan_details['initcovlimit'] - pdd) * .75
            OOP = pdd + ICL + gap
        if tds > plan_details['ccl']:
            # the total drug spend has exceeded $7,425.
            status = 'Catastrophic Coverage'
            ICL = (plan_details['initcovlimit'] - pdd) * .25
            gap = plan_details['trooplimit'] - ICL - pdd
            medICL = (plan_details['initcovlimit'] - pdd) * .75
            medcov = medICL + ((tds - plan_details['ccl']) * .95)
            catOOP = (tds - plan_details['ccl']) * .05
            OOP = pdd + ICL + gap + catOOP

    return status, OOP, medcov, ICL, gap

print(OOPCalc(plan_details))