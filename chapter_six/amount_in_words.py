ones = {
    0: "", 1: "ONE", 2: "TWO", 3: "THREE", 4: "FOUR",
    5: "FIVE", 6: "SIX", 7: "SEVEN", 8: "EIGHT", 9: "NINE",
    10: "TEN", 11: "ELEVEN", 12: "TWELVE", 13: "THIRTEEN",
    14: "FOURTEEN", 15: "FIFTEEN", 16: "SIXTEEN", 17: "SEVENTEEN",
    18: "EIGHTEEN", 19: "NINETEEN"
}
tens = {20: "TWENTY", 30: "THIRTY", 40: "FORTY", 50: "FIFTY",
        60: "SIXTY", 70: "SEVENTY", 80: "EIGHTY", 90: "NINETY"}

def num_to_words(number):
    if number < 20: return ones[number]
    elif number < 100: return tens[number // 10 * 10] + (" " + ones[number % 10] if number % 10 else "")
    elif number < 1000:
        return ones[number // 100] + " HUNDRED " + (num_to_words(number % 100) if number % 100 else "")

amount = 112.43
dollars, cents = str(amount).split(".")
dollars, cents = int(dollars), int(cents)

print(f"{num_to_words(dollars)} AND {cents}/100")
