class ConversationalSizingFitRecommenderClient:
    def recommend_best_fit(self, user_height_cm=178, user_weight_kg=72, garment_type='SLIM_FIT_BLAZER', user_fit_preference='TAILORED'):
        return {
            'fit_recommendation_id': 'fit_rec_8812',
            'recommended_size': '40R',
            'confidence_score': 0.94,
            'cross_brand_conversions': {'US': '40R', 'UK': '40R', 'EU': '50'},
            'fit_rationale': 'Based on 178cm/72kg and tailored preference, 40R provides optimal shoulder seam alignment without chest pulling.',
            'predicted_return_risk_pct': 4.2,
            'fit_profile_url': 'https://sizing.shop.genpark.ai/fits/8812.json'
        }
