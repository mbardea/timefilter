import timefilter.*

keep(1).today()
keep(7).past().week()
keep(6).past().month()
keep(8).past().year()
keep(1).daily()
keep(2).weekly()
keep(1).yearly()

run()

# time-filter.py --keep|--delete
