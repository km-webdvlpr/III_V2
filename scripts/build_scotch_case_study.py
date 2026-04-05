
from __future__ import annotations

import json
import random
from pathlib import Path

import matplotlib
import numpy as np
import pandas as pd

matplotlib.use("Agg")
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]
PROJECT_DIR = ROOT / "scotch-whisky-consumer-progression-intelligence"
ASSETS_DIR = PROJECT_DIR / "assets"
DATA_DIR = PROJECT_DIR / "data"
DOCS_DIR = PROJECT_DIR / "docs"

RANDOM_STATE = 42
rng = np.random.default_rng(RANDOM_STATE)
random.seed(RANDOM_STATE)


PRODUCTS = [
    {
        "brand": "Johnnie Walker",
        "expression": "Red Label",
        "whisky_type": "blend",
        "age_statement": np.nan,
        "peat_profile": "light",
        "tier": "entry",
        "base_price_750": 255,
        "pack_options": [750, 1000],
        "gift_box_rate": 0.08,
        "base_repeat": 0.12,
        "base_stage": ["entry", "familiar", "exploratory", "preference_led"],
        "stage_weights": [0.58, 0.27, 0.11, 0.04],
        "purchase_weights": [0.72, 0.12, 0.16],
        "role": "gateway",
    },
    {
        "brand": "Johnnie Walker",
        "expression": "Black Label",
        "whisky_type": "blend",
        "age_statement": 12,
        "peat_profile": "medium",
        "tier": "core",
        "base_price_750": 435,
        "pack_options": [750, 1000],
        "gift_box_rate": 0.31,
        "base_repeat": 0.26,
        "base_stage": ["entry", "familiar", "exploratory", "preference_led"],
        "stage_weights": [0.17, 0.44, 0.25, 0.14],
        "purchase_weights": [0.58, 0.18, 0.24],
        "role": "bridge",
    },
    {
        "brand": "Glenfiddich",
        "expression": "12",
        "whisky_type": "single_malt",
        "age_statement": 12,
        "peat_profile": "light",
        "tier": "premium",
        "base_price_750": 505,
        "pack_options": [700, 750],
        "gift_box_rate": 0.26,
        "base_repeat": 0.34,
        "base_stage": ["entry", "familiar", "exploratory", "preference_led"],
        "stage_weights": [0.09, 0.38, 0.31, 0.22],
        "purchase_weights": [0.62, 0.11, 0.27],
        "role": "gateway",
    },
    {
        "brand": "Glenlivet",
        "expression": "12",
        "whisky_type": "single_malt",
        "age_statement": 12,
        "peat_profile": "light",
        "tier": "premium",
        "base_price_750": 489,
        "pack_options": [700, 750],
        "gift_box_rate": 0.23,
        "base_repeat": 0.22,
        "base_stage": ["entry", "familiar", "exploratory", "preference_led"],
        "stage_weights": [0.12, 0.36, 0.32, 0.20],
        "purchase_weights": [0.60, 0.10, 0.30],
        "role": "trial",
    },
    {
        "brand": "Chivas Regal",
        "expression": "12",
        "whisky_type": "blend",
        "age_statement": 12,
        "peat_profile": "light",
        "tier": "core",
        "base_price_750": 399,
        "pack_options": [750, 1000],
        "gift_box_rate": 0.39,
        "base_repeat": 0.18,
        "base_stage": ["entry", "familiar", "exploratory", "preference_led"],
        "stage_weights": [0.21, 0.46, 0.21, 0.12],
        "purchase_weights": [0.46, 0.31, 0.23],
        "role": "gift_trial",
    },
    {
        "brand": "Monkey Shoulder",
        "expression": "Blended Malt",
        "whisky_type": "blend",
        "age_statement": np.nan,
        "peat_profile": "medium",
        "tier": "core",
        "base_price_750": 415,
        "pack_options": [750],
        "gift_box_rate": 0.16,
        "base_repeat": 0.21,
        "base_stage": ["entry", "familiar", "exploratory", "preference_led"],
        "stage_weights": [0.16, 0.31, 0.35, 0.18],
        "purchase_weights": [0.63, 0.07, 0.30],
        "role": "gateway",
    },
    {
        "brand": "Lagavulin",
        "expression": "16",
        "whisky_type": "single_malt",
        "age_statement": 16,
        "peat_profile": "heavy",
        "tier": "distinctive",
        "base_price_750": 1395,
        "pack_options": [750],
        "gift_box_rate": 0.43,
        "base_repeat": 0.38,
        "base_stage": ["entry", "familiar", "exploratory", "preference_led"],
        "stage_weights": [0.03, 0.15, 0.33, 0.49],
        "purchase_weights": [0.52, 0.18, 0.30],
        "role": "destination",
    },
    {
        "brand": "Laphroaig",
        "expression": "10",
        "whisky_type": "single_malt",
        "age_statement": 10,
        "peat_profile": "heavy",
        "tier": "distinctive",
        "base_price_750": 1045,
        "pack_options": [750],
        "gift_box_rate": 0.21,
        "base_repeat": 0.33,
        "base_stage": ["entry", "familiar", "exploratory", "preference_led"],
        "stage_weights": [0.04, 0.18, 0.42, 0.36],
        "purchase_weights": [0.60, 0.09, 0.31],
        "role": "destination",
    },
]

STORE_TYPES = ["liquor_store", "retail_chain", "premium_store"]
STORE_WEIGHTS = [0.48, 0.34, 0.18]
SHELF_ZONES = ["eye_level", "lower", "feature_display", "end_cap"]
DISPLAY_TYPES = ["standard", "promo_stack", "gift_section"]
PURCHASE_TYPES = ["self", "gift", "mixed"]
CITY_REGIONS = ["Sandton", "Rosebank", "Midrand", "Pretoria East", "Centurion", "Randburg", "Fourways", "East Rand", "West Rand", "Soweto"]
CITY_WEIGHTS = [0.13, 0.09, 0.11, 0.12, 0.10, 0.08, 0.11, 0.09, 0.08, 0.09]
STORE_DISPLAY_MAP = {
    "liquor_store": {"shelf_zone": [0.31, 0.29, 0.16, 0.24], "display_type": [0.55, 0.19, 0.26]},
    "retail_chain": {"shelf_zone": [0.28, 0.40, 0.17, 0.15], "display_type": [0.63, 0.25, 0.12]},
    "premium_store": {"shelf_zone": [0.38, 0.14, 0.26, 0.22], "display_type": [0.41, 0.10, 0.49]},
}
OCCASIONS = [
    "weekend top-up",
    "braai night",
    "quiet pour",
    "host gift",
    "corporate gift",
    "birthday run",
    "last-minute dinner",
    "special bottle",
    "month-end stock-up",
    "try something else",
]
OCCASION_WEIGHTS = [0.17, 0.11, 0.13, 0.12, 0.06, 0.08, 0.09, 0.08, 0.08, 0.08]
PRICE_BANDS = [
    (0, 360, "budget_edge"),
    (320, 520, "step_up"),
    (470, 760, "premium_window"),
    (690, 1100, "stretch"),
    (980, 2000, "top_shelf"),
]
DESC_PATTERNS = [
    "{brand} {expression} {pack}ml",
    "{brand} {expression} Scotch {pack}ml",
    "{brand} {expression} whisky",
    "{brand} {expression} gift pack",
    "{brand} {expression} single malt",
    "{brand} {expression} blend",
]
SHELF_TAG_PATTERNS = [
    "{brand} {expression} {pack}ML",
    "{brand} {expression} - R{price}",
    "{brand} {expression} whisky",
    "{brand} {expression} Gift",
    "{brand} {expression} {pack} ml",
    "{brand_short} {expression} {pack}",
]
PROMO_PATTERNS = [
    "2 for less on selected whisky",
    "gift ready bottle special",
    "premium pour week",
    "shelf talker only",
    "price drop while stock lasts",
    "bundle with glassware",
]
NOTE_SNIPPETS = [
    "shopper hovered, then came back after another aisle",
    "asked for something smoother than usual",
    "staff said peat was a hard sell here",
    "looked like a gift decision more than a regular buy",
    "buyer traded up from a usual blend",
    "picked from the feature end after a long look",
    "promo got attention but not a big basket",
    "repeat-looking purchase, no real hesitation",
    "buyer seemed curious, not fully convinced",
    "premium shelf got traffic, but not much conversion late week",
]
PRODUCT_WEIGHTS = [0.25, 0.16, 0.11, 0.09, 0.13, 0.14, 0.05, 0.07]


def ensure_dirs() -> None:
    for path in [PROJECT_DIR, ASSETS_DIR, DATA_DIR, DOCS_DIR]:
        path.mkdir(parents=True, exist_ok=True)


def weighted_choice(values, weights):
    return values[rng.choice(len(values), p=np.array(weights) / np.sum(weights))]


def choose_price_band(price: float) -> str:
    matches = [label for low, high, label in PRICE_BANDS if low <= price <= high]
    if not matches:
        return "top_shelf" if price > 1000 else "budget_edge"
    return random.choice(matches)


def build_product_desc(product: dict, pack_size_ml: int, gift_boxed: int) -> str:
    pattern = random.choice(DESC_PATTERNS)
    desc = pattern.format(brand=product["brand"], expression=product["expression"], pack=pack_size_ml)
    if gift_boxed and rng.random() < 0.55 and "gift" not in desc.lower():
        desc = f"{desc} gift box"
    return desc


def build_shelf_tag(product: dict, pack_size_ml: int, bottle_price: float) -> str:
    brand_short = "".join(word[0] for word in product["brand"].split())
    pattern = random.choice(SHELF_TAG_PATTERNS)
    tag = pattern.format(brand=product["brand"], expression=product["expression"], pack=pack_size_ml, price=int(round(bottle_price)), brand_short=brand_short)
    if rng.random() < 0.22:
        tag = tag.replace("ml", "ML").replace("whisky", "WHSKY")
    if rng.random() < 0.14:
        tag = tag.replace(" - ", " / ")
    if rng.random() < 0.08:
        tag = tag.replace("Johnnie Walker", "J Walker")
    return tag


def build_notes() -> str | float:
    if rng.random() < 0.34:
        return np.nan
    note = random.choice(NOTE_SNIPPETS)
    if rng.random() < 0.22:
        note = note[0].upper() + note[1:] + "."
    return note


def stage_num(stage: str) -> int:
    return {"entry": 1, "familiar": 2, "exploratory": 3, "preference_led": 4}[stage]


def generate_dataset(n_rows: int = 3200) -> pd.DataFrame:
    rows = []
    for _ in range(n_rows):
        product = PRODUCTS[rng.choice(len(PRODUCTS), p=PRODUCT_WEIGHTS)]
        stage = weighted_choice(product["base_stage"], product["stage_weights"])
        store_type = weighted_choice(STORE_TYPES, STORE_WEIGHTS)
        store_context = STORE_DISPLAY_MAP[store_type]
        shelf_zone = weighted_choice(SHELF_ZONES, store_context["shelf_zone"])
        display_type = weighted_choice(DISPLAY_TYPES, store_context["display_type"])
        purchase_type = weighted_choice(PURCHASE_TYPES, product["purchase_weights"])
        pack_size_ml = int(random.choice(product["pack_options"]))

        bottle_price = product["base_price_750"] * (pack_size_ml / 750) * rng.normal(1.0, 0.08)
        bottle_price *= {"liquor_store": 0.98, "retail_chain": 0.96, "premium_store": 1.07}[store_type]
        bottle_price *= {"eye_level": 1.01, "lower": 0.98, "feature_display": 1.0, "end_cap": 1.02}[shelf_zone]
        bottle_price = round(max(219, bottle_price), 2)

        promo_rate = 0.18 + (0.34 if display_type == "promo_stack" else 0) + (0.10 if shelf_zone == "feature_display" else 0)
        promo_rate -= 0.06 if product["tier"] == "distinctive" else 0
        promo_rate -= 0.02 if purchase_type == "gift" else 0
        promo_flag = int(rng.random() < np.clip(promo_rate, 0.03, 0.75))

        gift_boxed = int(rng.random() < product["gift_box_rate"])
        if rng.random() < 0.08:
            gift_boxed = 1 - gift_boxed
        if gift_boxed and purchase_type == "self" and rng.random() < 0.34:
            purchase_type = "gift"
        elif gift_boxed and purchase_type == "mixed" and rng.random() < 0.28:
            purchase_type = "gift"
        elif display_type == "gift_section" and purchase_type == "self" and rng.random() < 0.18:
            purchase_type = "mixed"

        occasion = weighted_choice(OCCASIONS, OCCASION_WEIGHTS)
        if purchase_type == "self" and occasion in {"host gift", "corporate gift"} and rng.random() < 0.75:
            occasion = "quiet pour"
        if purchase_type == "gift" and occasion in {"weekend top-up", "month-end stock-up"} and rng.random() < 0.70:
            occasion = "host gift"
        if rng.random() < 0.24:
            occasion = np.nan

        basket_role = "primary"
        if pack_size_ml == 750 and bottle_price < 460 and rng.random() < 0.28:
            basket_role = "add_on"
        if purchase_type == "gift" and rng.random() < 0.84:
            basket_role = "primary"

        repeat_score = product["base_repeat"]
        repeat_score += 0.09 if purchase_type == "self" else -0.03
        repeat_score += 0.07 if stage in {"familiar", "preference_led"} else -0.02
        repeat_score += 0.06 if display_type == "standard" else -0.01
        repeat_score += 0.04 if product["role"] == "destination" else 0
        repeat_score += 0.03 if product["role"] == "bridge" else 0
        repeat_score -= 0.06 if promo_flag else 0
        repeat_score -= 0.05 if purchase_type == "gift" else 0
        repeat_score -= 0.04 if product["role"] == "trial" else 0
        repeat_purchase_flag = int(rng.random() < np.clip(repeat_score, 0.03, 0.68))
        if rng.random() < 0.05:
            repeat_purchase_flag = 1 - repeat_purchase_flag

        if repeat_purchase_flag:
            days_since_last_purchase = int(max(5, rng.normal(34 if product["tier"] != "distinctive" else 49, 17)))
        else:
            days_since_last_purchase = np.nan if rng.random() < 0.57 else int(max(9, rng.normal(69, 31)))

        units_bought = 1
        if purchase_type == "gift" and rng.random() < 0.16:
            units_bought = 2
        elif promo_flag and product["tier"] in {"entry", "core"} and rng.random() < 0.17:
            units_bought = 2
        elif repeat_purchase_flag and pack_size_ml < 1000 and rng.random() < 0.08:
            units_bought = 2

        stage_value = stage_num(stage)
        if product["tier"] == "distinctive" and stage == "entry" and rng.random() < 0.62:
            stage_value = min(4, stage_value + 1)
        if promo_flag and product["role"] == "gateway" and rng.random() < 0.16:
            stage_value = max(1, stage_value - 1)
        estimated_buyer_stage = {1: "entry", 2: "familiar", 3: "exploratory", 4: "preference_led"}[stage_value]

        promo_text = np.nan
        if promo_flag:
            promo_text = random.choice(PROMO_PATTERNS)
            if gift_boxed and rng.random() < 0.27:
                promo_text = "gift box offer"

        rows.append(
            {
                "brand": product["brand"],
                "expression": product["expression"],
                "whisky_type": product["whisky_type"],
                "age_statement": product["age_statement"],
                "pack_size_ml": pack_size_ml,
                "bottle_price": bottle_price,
                "price_band": choose_price_band(bottle_price),
                "is_gift_boxed": gift_boxed,
                "peat_profile": product["peat_profile"],
                "tier": product["tier"],
                "store_type": store_type,
                "shelf_zone": shelf_zone,
                "display_type": display_type,
                "promo_flag": promo_flag,
                "city_region": weighted_choice(CITY_REGIONS, CITY_WEIGHTS),
                "week": int(rng.integers(1, 53)),
                "purchase_type": purchase_type,
                "occasion": occasion,
                "basket_role": basket_role,
                "repeat_purchase_flag": repeat_purchase_flag,
                "days_since_last_purchase": days_since_last_purchase,
                "units_bought": units_bought,
                "estimated_buyer_stage": estimated_buyer_stage,
                "product_desc_raw": build_product_desc(product, pack_size_ml, gift_boxed),
                "shelf_tag_raw": build_shelf_tag(product, pack_size_ml, bottle_price),
                "promo_text_raw": promo_text,
                "notes_text": build_notes(),
            }
        )

    return pd.DataFrame(rows)


def add_metric_card(value: str, label: str, copy: str) -> str:
    return f"""
<div class="report-card">
  <div class="report-card__label">{label}</div>
  <div class="report-card__value">{value}</div>
  <p class="report-card__copy">{copy}</p>
</div>
""".strip()


def save_chart_tier_distribution(df: pd.DataFrame) -> None:
    summary = df.groupby("tier").agg(observations=("brand", "size"), avg_price=("bottle_price", "mean")).reindex(["entry", "core", "premium", "distinctive"]).reset_index()
    fig, ax = plt.subplots(figsize=(10, 5.5), facecolor="#0d1a12")
    ax.set_facecolor("#111d16")
    bars = ax.bar(summary["tier"], summary["observations"], color=["#3d9970", "#74b67a", "#d8b15c", "#b47a44"])
    ax2 = ax.twinx()
    ax2.plot(summary["tier"], summary["avg_price"], color="#f5f0e8", marker="o", linewidth=2)
    ax.tick_params(colors="#f5f0e8")
    ax2.tick_params(colors="#c8c0ac")
    ax.set_ylabel("Observations", color="#f5f0e8")
    ax2.set_ylabel("Average bottle price (R)", color="#c8c0ac")
    ax.set_title("Entry volume still dominates, but price lifts hard higher up the ladder", color="#f5f0e8", pad=14)
    for bar in bars:
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 22, f"{int(bar.get_height())}", ha="center", color="#c8c0ac", fontsize=9)
    plt.tight_layout()
    fig.savefig(ASSETS_DIR / "tier-distribution.png", dpi=180, facecolor=fig.get_facecolor())
    plt.close(fig)


def save_chart_progression_map(df: pd.DataFrame) -> None:
    summary = df.assign(product_key=df["brand"] + " " + df["expression"].astype(str)).groupby("product_key").agg(
        avg_price=("bottle_price", "mean"),
        repeat_rate=("repeat_purchase_flag", "mean"),
        self_share=("purchase_type", lambda s: (s == "self").mean()),
        observations=("brand", "size"),
    ).reset_index()
    summary["trial_score"] = (1 - summary["repeat_rate"]) * summary["observations"] * summary["self_share"]
    fig, ax = plt.subplots(figsize=(10.2, 6), facecolor="#0d1a12")
    ax.set_facecolor("#111d16")
    scatter = ax.scatter(summary["avg_price"], summary["repeat_rate"] * 100, s=np.clip(summary["observations"] * 0.35, 70, 320), c=summary["trial_score"], cmap="copper", edgecolor="#f5f0e8", alpha=0.9)
    ax.set_xlabel("Average bottle price (R)", color="#f5f0e8")
    ax.set_ylabel("Repeat purchase rate (%)", color="#f5f0e8")
    ax.tick_params(colors="#f5f0e8")
    ax.set_title("Gateway products sit low-to-mid price with discovery; destinations keep the repeat", color="#f5f0e8", pad=14)
    for _, row in summary.iterrows():
        ax.annotate(row["product_key"], (row["avg_price"], row["repeat_rate"] * 100), xytext=(6, 6), textcoords="offset points", color="#c8c0ac", fontsize=8)
    cbar = fig.colorbar(scatter, ax=ax)
    cbar.ax.tick_params(colors="#c8c0ac")
    cbar.set_label("Trial-heavy score", color="#c8c0ac")
    plt.tight_layout()
    fig.savefig(ASSETS_DIR / "progression-map.png", dpi=180, facecolor=fig.get_facecolor())
    plt.close(fig)


def save_chart_price_friction(df: pd.DataFrame) -> None:
    labels = ["<320", "320-419", "420-519", "520-699", "700-949", "950-1399", "1400+"]
    temp = df.copy()
    temp["price_step"] = pd.cut(temp["bottle_price"], bins=[0, 320, 420, 520, 700, 950, 1400, 1800], labels=labels, include_lowest=True)
    summary = temp.groupby("price_step", observed=False).agg(
        repeat_rate=("repeat_purchase_flag", "mean"),
        exploratory_share=("estimated_buyer_stage", lambda s: s.isin(["exploratory", "preference_led"]).mean()),
        observations=("brand", "size"),
    ).reset_index()
    fig, ax = plt.subplots(figsize=(10.4, 5.4), facecolor="#0d1a12")
    ax.set_facecolor("#111d16")
    ax.plot(summary["price_step"].astype(str), summary["exploratory_share"] * 100, marker="o", linewidth=2.2, color="#d8b15c", label="Exploratory or preference-led share")
    ax.plot(summary["price_step"].astype(str), summary["repeat_rate"] * 100, marker="o", linewidth=2.2, color="#3d9970", label="Repeat rate")
    ax.set_ylabel("% of observations", color="#f5f0e8")
    ax.set_xlabel("Bottle price step (R)", color="#f5f0e8")
    ax.tick_params(colors="#f5f0e8")
    ax.set_title("Progression asks get accepted up to a point, then the stretch becomes obvious", color="#f5f0e8", pad=14)
    ax.legend(frameon=False, labelcolor="#c8c0ac")
    plt.tight_layout()
    fig.savefig(ASSETS_DIR / "price-friction.png", dpi=180, facecolor=fig.get_facecolor())
    plt.close(fig)


def save_chart_packaging(df: pd.DataFrame) -> None:
    summary = df.groupby("is_gift_boxed").agg(
        gift_share=("purchase_type", lambda s: (s == "gift").mean()),
        repeat_rate=("repeat_purchase_flag", "mean"),
        observations=("brand", "size"),
    ).reset_index()
    summary["segment"] = summary["is_gift_boxed"].map({0: "Not gift boxed", 1: "Gift boxed"})
    fig, ax = plt.subplots(figsize=(8.8, 5.4), facecolor="#0d1a12")
    ax.set_facecolor("#111d16")
    x = np.arange(len(summary))
    width = 0.34
    ax.bar(x - width / 2, summary["gift_share"] * 100, width, color="#b47a44", label="Gift purchase share")
    ax.bar(x + width / 2, summary["repeat_rate"] * 100, width, color="#3d9970", label="Repeat rate")
    ax.set_xticks(x, summary["segment"])
    ax.set_ylabel("% of observations", color="#f5f0e8")
    ax.tick_params(colors="#f5f0e8")
    ax.set_title("Gift boxes widen gifting behaviour more than they build repeat", color="#f5f0e8", pad=14)
    ax.legend(frameon=False, labelcolor="#c8c0ac")
    plt.tight_layout()
    fig.savefig(ASSETS_DIR / "packaging-gifting.png", dpi=180, facecolor=fig.get_facecolor())
    plt.close(fig)


def save_chart_display(df: pd.DataFrame) -> None:
    summary = df.groupby("display_type").agg(
        exploratory_share=("estimated_buyer_stage", lambda s: s.isin(["entry", "exploratory"]).mean()),
        repeat_rate=("repeat_purchase_flag", "mean"),
    ).reindex(["standard", "promo_stack", "gift_section"]).reset_index()
    fig, ax = plt.subplots(figsize=(9.5, 5.3), facecolor="#0d1a12")
    ax.set_facecolor("#111d16")
    ax.bar(summary["display_type"], summary["exploratory_share"] * 100, color="#d8b15c", alpha=0.86, label="Discovery-oriented share")
    ax.plot(summary["display_type"], summary["repeat_rate"] * 100, marker="o", linewidth=2.3, color="#f5f0e8", label="Repeat rate")
    ax.set_ylabel("% of observations", color="#f5f0e8")
    ax.tick_params(colors="#f5f0e8")
    ax.set_title("Feature-led discovery is real, but the standard shelf still carries loyalty", color="#f5f0e8", pad=14)
    ax.legend(frameon=False, labelcolor="#c8c0ac")
    plt.tight_layout()
    fig.savefig(ASSETS_DIR / "display-influence.png", dpi=180, facecolor=fig.get_facecolor())
    plt.close(fig)


def save_chart_stalling(df: pd.DataFrame) -> None:
    temp = df.copy()
    temp["progression_state"] = np.select(
        [
            (temp["tier"].isin(["entry", "core"])) & (temp["estimated_buyer_stage"] == "entry"),
            (temp["tier"].isin(["premium", "distinctive"])) & (temp["repeat_purchase_flag"] == 0),
            (temp["tier"].isin(["premium", "distinctive"])) & (temp["repeat_purchase_flag"] == 1),
            (temp["promo_flag"] == 1) & (temp["tier"].isin(["core", "premium"])),
        ],
        ["Stayed accessible", "Tried up, did not return", "Traded up and returned", "Needed promo support"],
        default="Other",
    )
    summary = temp["progression_state"].value_counts().reindex(["Stayed accessible", "Tried up, did not return", "Traded up and returned", "Needed promo support", "Other"]).fillna(0).astype(int).reset_index()
    summary.columns = ["progression_state", "observations"]
    fig, ax = plt.subplots(figsize=(10.2, 5.5), facecolor="#0d1a12")
    ax.set_facecolor("#111d16")
    ax.barh(summary["progression_state"], summary["observations"], color=["#3d9970", "#b47a44", "#d8b15c", "#74b67a", "#33443a"])
    ax.set_xlabel("Observations", color="#f5f0e8")
    ax.tick_params(colors="#f5f0e8")
    ax.set_title("The dataset leaves a lot of evidence of stall, not just clean upward movement", color="#f5f0e8", pad=14)
    plt.tight_layout()
    fig.savefig(ASSETS_DIR / "stalling-points.png", dpi=180, facecolor=fig.get_facecolor())
    plt.close(fig)


def export_charts(df: pd.DataFrame) -> None:
    save_chart_tier_distribution(df)
    save_chart_progression_map(df)
    save_chart_price_friction(df)
    save_chart_packaging(df)
    save_chart_display(df)
    save_chart_stalling(df)


def write_insights(df: pd.DataFrame) -> dict[str, str]:
    product_view = df.assign(product_key=df["brand"] + " " + df["expression"].astype(str)).groupby("product_key").agg(
        observations=("brand", "size"),
        repeat_rate=("repeat_purchase_flag", "mean"),
        entry_familiar_share=("estimated_buyer_stage", lambda s: s.isin(["entry", "familiar"]).mean()),
        preference_share=("estimated_buyer_stage", lambda s: s.isin(["exploratory", "preference_led"]).mean()),
        avg_price=("bottle_price", "mean"),
        self_share=("purchase_type", lambda s: (s == "self").mean()),
        tier=("tier", "first"),
    ).reset_index()
    product_view["gateway_score"] = product_view["observations"] * (product_view["entry_familiar_share"] * 0.62 + product_view["preference_share"] * 0.38) * product_view["self_share"] * (product_view["avg_price"] / 420).clip(0.85, 1.35) * (1 - (product_view["repeat_rate"] - 0.28).abs())
    product_view["destination_score"] = product_view["repeat_rate"] * product_view["preference_share"] * np.log1p(product_view["avg_price"])
    gateway_candidates = product_view[product_view["tier"].isin(["core", "premium"])].copy()
    gateway_product = gateway_candidates.sort_values("gateway_score", ascending=False).iloc[0]["product_key"]
    destination_product = product_view.sort_values("destination_score", ascending=False).iloc[0]["product_key"]

    friction_table = df.assign(price_step=pd.cut(df["bottle_price"], bins=[0, 320, 420, 520, 700, 950, 1400, 1800], include_lowest=True).astype(str)).groupby("price_step").agg(repeat_rate=("repeat_purchase_flag", "mean")).reset_index()
    friction_table["drop_vs_prev"] = friction_table["repeat_rate"].diff()
    raw_friction_step = friction_table.sort_values("drop_vs_prev").iloc[0]["price_step"]
    biggest_friction_step = raw_friction_step.replace("(320.0, 420.0]", "R320-R420").replace("(420.0, 520.0]", "R420-R520").replace("(520.0, 700.0]", "R520-R700").replace("(700.0, 950.0]", "R700-R950").replace("(950.0, 1400.0]", "R950-R1400").replace("(-0.001, 320.0]", "Under R320").replace("(1400.0, 1800.0]", "R1400+")
    key_signal = "Gateway bottles are not just cheaper; they are the ones that still look safe enough for self-purchase while nudging shoppers into a clearer style cue or price step."

    insights = f"""INSIGHT
Gateway movement starts with familiar labels, not dramatic leaps.
FINDING
{gateway_product} shows the strongest mix of volume, entry-to-familiar buyer presence, and enough self-purchase behaviour to act like a progression bridge rather than a dead-end bargain buy.
SO WHAT
Progression is easier when the step-up still feels recognisable. Shoppers do not suddenly become premium buyers; they usually step into something that feels slightly more deliberate, not completely unfamiliar.
RECOMMENDATION
Use gateway bottles to frame the category ladder on shelf. Keep them visible near stronger premium cues instead of isolating them in the value block.

INSIGHT
Some premium bottles earn curiosity faster than they earn loyalty.
FINDING
Glenlivet 12 and gift-forward Chivas Regal 12 patterns lean more heavily toward trial than repeat, especially when the purchase sits in a gift section or a promo-led context.
SO WHAT
A bottle can look healthy in a discovery moment without becoming part of someone's personal rotation. That matters if the goal is progression, not just one-off uplift.
RECOMMENDATION
Treat these as recruitment products. Support them with education, pairing, or trade-up prompts rather than assuming trial will naturally convert into loyalty.

INSIGHT
Price progression gets noticeably tighter around {biggest_friction_step}.
FINDING
The modeled repeat signal softens most sharply once shoppers stretch into this price step, even though exploratory interest keeps rising.
SO WHAT
People are willing to browse upward before they are willing to live there. Interest is not the same thing as comfort.
RECOMMENDATION
Make the step feel smaller with shelf comparison, tasting cues, or a clear why-this-costs-more story.

INSIGHT
Gift boxes help trial more than they help habit.
FINDING
Gift-boxed bottles over-index in gift buying and feature-led display moments, but they do not turn into the strongest repeat performers in the dataset.
SO WHAT
Packaging can open the door without creating a relationship. That is useful, but it should not be mistaken for loyalty.
RECOMMENDATION
Use gift packaging as a seasonal acquisition tool, then hand off repeat-building to the standard shelf, price architecture, and flavour clarity.

INSIGHT
Standard shelf placement still matters more for loyalty than flashy displays do.
FINDING
Promo stacks and gift sections help discovery, but repeat comes through more steadily on standard display conditions where shoppers look like they already know what they want.
SO WHAT
Discovery and loyalty are not built in the same place. A display that gets attention is not automatically the one that builds a base.
RECOMMENDATION
Separate recruitment space from habit space in retail planning. Feature displays should seed trial; core shelf placement should protect follow-up purchase.

INSIGHT
Destination bottles are defined by commitment, not just price.
FINDING
{destination_product} has the strongest destination pattern: lower broad frequency, stronger repeat, and a heavier concentration of exploratory and preference-led buyers.
SO WHAT
The top end is not where most people start, but it is where a smaller set of buyers become much clearer about what they like.
RECOMMENDATION
Merchandise destination products with flavour language and confidence cues, not only prestige cues. People need permission to commit, not just admire.
"""
    (PROJECT_DIR / "insights.md").write_text(insights, encoding="utf-8")
    return {"signal": key_signal, "friction": biggest_friction_step, "gateway": gateway_product, "destination": destination_product}


def create_notebook(summary_text: dict[str, str]) -> None:
    cells = [
        {"cell_type": "markdown", "metadata": {}, "source": ["# Scotch Whisky: Consumer Progression & Premiumization Intelligence\n", "\n", "A product intelligence case study looking at how shoppers move from accessible Scotch into more distinctive premium expressions, and where shelf context, gifting, and price steps help or interrupt that journey.\n"]},
        {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": ["import pandas as pd\n", "import numpy as np\n", "import matplotlib.pyplot as plt\n", "from pathlib import Path\n", "\n", "plt.style.use('dark_background')\n", "base = Path.cwd()\n", "df = pd.read_csv(base / 'data' / 'scotch_progression_observations.csv') if (base / 'data').exists() else pd.read_csv(base / 'scotch-whisky-consumer-progression-intelligence' / 'data' / 'scotch_progression_observations.csv')\n", "df.head()\n"]},
    ]
    sections = [
        ("1. Dataset Overview & Imperfection Notes", "Does this still feel like shelf reality, or did we accidentally clean the life out of it?", ["sample = df[['brand','expression','tier','bottle_price','price_band','purchase_type','repeat_purchase_flag']].sample(10, random_state=42)\n", "sample\n", "\n", "imperfections = pd.DataFrame({\n", "    'metric': ['rows', 'missing occasion %', 'missing notes %', 'gift boxed share %', 'repeat share %'],\n", "    'value': [len(df), round(df['occasion'].isna().mean()*100,1), round(df['notes_text'].isna().mean()*100,1), round(df['is_gift_boxed'].mean()*100,1), round(df['repeat_purchase_flag'].mean()*100,1)]\n", "})\n", "imperfections\n"], "The case keeps missing occasion and notes fields, rough shelf text, and imperfect repeat signals on purpose. It should feel like something assembled from retail observation, not a polished CRM export."),
        ("2. Product Tier Distribution", "Where does the category still live day to day, and where does value start to thin out?", ["tier_summary = df.groupby('tier').agg(observations=('brand','size'), avg_price=('bottle_price','mean')).reindex(['entry','core','premium','distinctive'])\n", "tier_summary\n", "fig, ax = plt.subplots(figsize=(8,4.5))\n", "ax.bar(tier_summary.index, tier_summary['observations'], color=['#3d9970','#74b67a','#d8b15c','#b47a44'])\n", "ax.set_title('Tier distribution')\n", "ax.set_ylabel('Observations')\n", "plt.show()\n"], "Entry and core should still hold most of the weekly traffic. Premium and distinctive matter because they change value, preference, and confidence, not because they overpower the category by count."),
        ("3. Price Step & Progression Friction", f"At what point do shoppers look interested in trading up, but stop looking comfortable doing it repeatedly? The sharpest friction shows up around {summary_text['friction']}.", ["price_bins = pd.cut(df['bottle_price'], bins=[0,320,420,520,700,950,1400,1800], include_lowest=True)\n", "price_friction = df.assign(price_step=price_bins.astype(str)).groupby('price_step').agg(repeat_rate=('repeat_purchase_flag','mean'), exploratory_share=('estimated_buyer_stage', lambda s: s.isin(['exploratory','preference_led']).mean()), observations=('brand','size')).reset_index()\n", "price_friction\n", "fig, ax = plt.subplots(figsize=(9,4.6))\n", "ax.plot(price_friction['price_step'], price_friction['repeat_rate']*100, marker='o', label='Repeat rate')\n", "ax.plot(price_friction['price_step'], price_friction['exploratory_share']*100, marker='o', label='Exploratory or preference-led share')\n", "ax.legend()\n", "plt.xticks(rotation=20)\n", "plt.show()\n"], "The useful read is where curiosity keeps climbing without repeat climbing with it. That is usually where premiumization is visible, but not yet comfortable."),
        ("4. Packaging & Gifting Behaviour", "Does gift packaging recruit people into premium Scotch, or does it just create a good one-off occasion?", ["packaging = df.groupby('is_gift_boxed').agg(gift_share=('purchase_type', lambda s: (s == 'gift').mean()), repeat_rate=('repeat_purchase_flag','mean'), avg_price=('bottle_price','mean')).reset_index()\n", "packaging['segment'] = packaging['is_gift_boxed'].map({0:'not gift boxed',1:'gift boxed'})\n", "packaging\n"], "Gift packaging can widen the top of the funnel without earning a lasting place in the shopper's own routine. That difference matters."),
        ("5. Retail Display Influence", "Which retail environments help discovery, and which ones actually hold repeat?", ["display = df.groupby('display_type').agg(discovery_share=('estimated_buyer_stage', lambda s: s.isin(['entry','exploratory']).mean()), repeat_rate=('repeat_purchase_flag','mean'), promo_share=('promo_flag','mean')).reset_index()\n", "display\n"], "Feature displays should help bottles get noticed. The standard shelf is where preference often shows itself with less theatre."),
        ("6. Repeat Purchase vs Trial Behaviour", f"Which products are opening the door, and which ones look like places people eventually settle? Gateway: {summary_text['gateway']}. Destination: {summary_text['destination']}.", ["product_view = df.assign(product_key=df['brand'] + ' ' + df['expression'].astype(str)).groupby('product_key').agg(observations=('brand','size'), repeat_rate=('repeat_purchase_flag','mean'), avg_price=('bottle_price','mean'), self_share=('purchase_type', lambda s: (s == 'self').mean())).sort_values('observations', ascending=False)\n", "product_view\n"], "Gateway products still need enough self-purchase comfort to recruit buyers. Destination products matter because a smaller set of shoppers keep coming back to them."),
        ("7. Progression Signals & Stalling Points", f"Where do we see genuine movement upward, and where do shoppers appear to hesitate, bounce, or need support? Key read: {summary_text['signal']}", ["stall = df.copy()\n", "stall['progression_state'] = np.select([(stall['tier'].isin(['entry','core'])) & (stall['estimated_buyer_stage'] == 'entry'), (stall['tier'].isin(['premium','distinctive'])) & (stall['repeat_purchase_flag'] == 0), (stall['tier'].isin(['premium','distinctive'])) & (stall['repeat_purchase_flag'] == 1), (stall['promo_flag'] == 1) & (stall['tier'].isin(['core','premium']))], ['Stayed accessible','Tried up, did not return','Traded up and returned','Needed promo support'], default='Other')\n", "stall['progression_state'].value_counts()\n"], "Not all movement upward is healthy. Some bottles create curiosity without conviction, while others quietly build a smaller but stronger preference base."),
        ("8. Key Commercial Insights", "What should a commercial or category team actually do with this?", [], "The category still recruits through familiar entry points, but loyalty sits closer to confidence than promotion. Gift packaging helps reach, standard shelf helps repeat, and the price ladder needs clearer hand-holds once the stretch becomes visible."),
    ]
    for heading, question, code_lines, commentary in sections:
        cells.append({"cell_type": "markdown", "metadata": {}, "source": [f"## {heading}\n", "\n", f"**Question:** {question}\n", "\n", f"{commentary}\n"]})
        if code_lines:
            cells.append({"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": code_lines})

    notebook = {"cells": cells, "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}, "language_info": {"name": "python", "version": "3.13"}}, "nbformat": 4, "nbformat_minor": 5}
    (PROJECT_DIR / "scotch_progression_intelligence.ipynb").write_text(json.dumps(notebook, indent=2), encoding="utf-8")


def create_docs_page(df: pd.DataFrame, summary_text: dict[str, str]) -> None:
    avg_price = round(df["bottle_price"].mean(), 0)
    repeat_rate = round(df["repeat_purchase_flag"].mean() * 100, 1)
    missing_notes = round(df["notes_text"].isna().mean() * 100, 1)
    title = "Scotch Whisky: Consumer Progression & Premiumization Intelligence"
    html = f"""---
layout: default
title: "{title}"
description: "A product intelligence case study on how Scotch shoppers move from accessible bottles into more distinctive premium expressions."
---
<main class="site-main site-main--project">
  <section class="dossier-header">
    <div class="breadcrumb">
      <a href="{{{{ '/' | relative_url }}}}">HOME</a><span>//</span>
      <a href="{{{{ '/projects/' | relative_url }}}}">PROJECTS</a><span>//</span>
      SCOTCH WHISKY INTELLIGENCE
    </div>
    <div class="dossier-meta">
      <span class="dossier-type">PRODUCT INTELLIGENCE | BEVERAGE RETAIL</span>
      <span class="dossier-date">2026-04-05</span>
      <span class="dossier-id">CASE FILE // LOG-22</span>
    </div>
    <h1 class="dossier-title">{title}</h1>
    <p class="dossier-lede">A Scotch category case study focused on progression, premiumization, and the shelf signals that either help a buyer move up or send them back to what already feels safe.</p>
    <div class="dossier-tags"><span class="dtag">#Python</span><span class="dtag">#RetailIntelligence</span><span class="dtag">#ConsumerBehaviour</span><span class="dtag">#BeverageAnalytics</span></div>
    <div class="dossier-cta"><a href="{{{{ '/projects/scotch-whisky-consumer-progression-intelligence/' | relative_url }}}}" class="cta-btn ghost">Open case file</a></div>
  </section>
  <section class="case-layout">
    <aside class="sidebar sidebar--project">
      <div class="sidebar-label">// SECTIONS</div>
      <a class="sidebar-link" href="#problem">Problem</a>
      <a class="sidebar-link" href="#approach">Approach</a>
      <a class="sidebar-link" href="#insights">Key insights</a>
      <a class="sidebar-link" href="#visuals">Visual highlights</a>
      <a class="sidebar-link" href="#implications">Commercial implications</a>
      <a class="sidebar-link" href="#tools">Tools used</a>
      <hr class="sidebar-divider">
      <div class="sidebar-label">// QUICK READ</div>
      <div class="sidebar-link sidebar-link--static">Gateway: {summary_text['gateway']}</div>
      <div class="sidebar-link sidebar-link--static">Destination: {summary_text['destination']}</div>
      <div class="sidebar-link sidebar-link--static">Friction: {summary_text['friction']}</div>
    </aside>
    <article class="case-body">
      <div class="snapshot-strip reveal visible">
        <div class="snap-cell"><span class="snap-label">Problem</span><span class="snap-copy">Category performance alone does not show when a shopper is genuinely trading up versus just reacting to a gift moment or promotion.</span></div>
        <div class="snap-cell"><span class="snap-label">Focus</span><span class="snap-copy">This build tracks product role, shelf context, gifting cues, and repeat behaviour to read progression in a more believable retail way.</span></div>
        <div class="snap-cell"><span class="snap-label">Outcome</span><span class="snap-copy">The analysis isolates gateway products, destination products, visible price friction, and where retail presentation changes the path.</span></div>
      </div>
      <div class="project-content">
        <h2 id="problem">Problem statement</h2>
        <p>The real question is not which Scotch sells the most. It is whether the shelf shows signs that a shopper is learning, stretching, settling into a preference, or backing away once the next bottle feels like too much of a leap.</p>
        <p>This makes the case more useful for product and commercial teams. We are reading a progression journey through bottle choice, price steps, display conditions, gifting behaviour, and rough repeat signals rather than pretending we have a perfect customer history.</p>
        <div class="report-grid">{add_metric_card(f'{len(df):,}', 'OBSERVATIONS', 'Synthetic purchase and exposure moments across eight Scotch expressions and Gauteng-oriented retail contexts.')}{add_metric_card(f'R{int(avg_price)}', 'AVERAGE BOTTLE PRICE', 'The average sits in the middle, but the range still shows a very visible stretch into distinctive territory.')}{add_metric_card(f'{repeat_rate}%', 'REPEAT SHARE', 'Repeat is present, but it is sparse enough to stay believable instead of acting like a clean loyalty truth.')}{add_metric_card(summary_text['gateway'], 'STRONGEST GATEWAY', 'The best gateway product combines recognisable comfort with a credible next step into more deliberate Scotch buying.')}{add_metric_card(summary_text['destination'], 'STRONGEST DESTINATION', 'The destination bottle draws fewer shoppers overall but keeps a stronger commitment once the buyer has found their lane.')}{add_metric_card(f'{missing_notes}%', 'MISSING NOTES', 'The text fields stay imperfect on purpose so the case feels closer to messy retail observation than a lab exercise.')}</div>
        <h2 id="approach">Approach</h2>
        <p>The dataset was built around three layers of reality: the bottle itself, the retail setting around it, and the behavioural hints left behind by the purchase moment. That keeps the analysis grounded in product role and shelf context instead of slipping into generic FMCG reporting.</p>
        <p>The model allows missing occasion and notes values, messy shelf tags, overlapping price bands, inconsistent gift-box logic, and uneven repeat signals. Premium bottles are lower-frequency but higher-value. Entry bottles still dominate volume. Some products recruit trial better than they hold repeat. Others do the opposite.</p>
        <h2 id="insights">Key insights</h2>
        <p><strong>Gateway products are doing more than discount work.</strong> {summary_text['gateway']} looks strongest when the shopper wants to step up without feeling like they are abandoning familiar territory.</p>
        <p><strong>The price ladder gets sticky at {summary_text['friction']}.</strong> Exploratory interest keeps climbing there, but repeat starts to loosen. That is usually where curiosity stops being the same thing as comfort.</p>
        <p><strong>Gift packaging creates reach, not necessarily routine.</strong> It helps bottles get bought for occasions and display-led moments, but the standard shelf still carries more of the loyalty story.</p>
        <p><strong>Destination products are defined by commitment.</strong> {summary_text['destination']} stands out not because it wins volume, but because it concentrates a clearer kind of preference once a buyer is ready for it.</p>
        <h2 id="visuals">Visual highlights</h2>
        <div class="report-figure"><img src="{{{{ '/scotch-whisky-consumer-progression-intelligence/assets/tier-distribution.png' | relative_url }}}}" alt="Tier distribution chart for Scotch whisky case study" /><p class="report-caption">Entry and core still carry the day-to-day traffic, while premium and distinctive expressions sharply lift average bottle price without pretending to be the whole category.</p></div>
        <div class="report-figure"><img src="{{{{ '/scotch-whisky-consumer-progression-intelligence/assets/progression-map.png' | relative_url }}}}" alt="Progression map chart for Scotch whisky case study" /><p class="report-caption">Gateway bottles sit in the lower-to-middle price band with broader trial. Destination bottles are smaller in raw count but meaningfully stronger on repeat.</p></div>
        <div class="report-figure"><img src="{{{{ '/scotch-whisky-consumer-progression-intelligence/assets/price-friction.png' | relative_url }}}}" alt="Price friction chart for Scotch whisky case study" /><p class="report-caption">The progression story tightens at the stretch point. People keep looking upward before they fully agree to live there.</p></div>
        <div class="report-figure"><img src="{{{{ '/scotch-whisky-consumer-progression-intelligence/assets/display-influence.png' | relative_url }}}}" alt="Retail display influence chart for Scotch whisky case study" /><p class="report-caption">Feature-led discovery matters, but repeat is steadier where the bottle remains easy to find without spectacle.</p></div>
        <h2 id="implications">Commercial implications</h2>
        <p>Merchandise gateway bottles near visible step-up cues rather than leaving them stranded in the value section. The point is to make progression feel legible.</p>
        <p>Treat gift packaging as recruitment. If the goal is loyalty, the follow-up needs to happen through standard shelf presence, flavour clarity, and a less intimidating price ladder.</p>
        <p>Do not confuse premium traffic with premium commitment. A bottle can get attention from a gift display and still fail to become a self-driven repeat choice.</p>
        <h2 id="tools">Tools used</h2>
        <p>Python, pandas, numpy, matplotlib, Jupyter notebook structure, GitHub Pages-ready HTML, and a synthetic dataset built to stay slightly untidy on purpose.</p>
        <p><a href="{{{{ '/projects/' | relative_url }}}}">Back to the III.IV project archive</a></p>
      </div>
    </article>
  </section>
</main>
"""
    (DOCS_DIR / "index.html").write_text(html, encoding="utf-8")


def main() -> None:
    ensure_dirs()
    df = generate_dataset()
    df.to_csv(DATA_DIR / "scotch_progression_observations.csv", index=False)
    export_charts(df)
    summary_text = write_insights(df)
    create_notebook(summary_text)
    create_docs_page(df, summary_text)
    manifest = {
        "dataset_rows": int(len(df)),
        "gateway_product": summary_text["gateway"],
        "destination_product": summary_text["destination"],
        "biggest_friction_step": summary_text["friction"],
        "key_signal": summary_text["signal"],
    }
    (PROJECT_DIR / "build_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
