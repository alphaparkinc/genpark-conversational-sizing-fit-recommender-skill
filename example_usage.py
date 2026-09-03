from client import ConversationalSizingFitRecommenderClient

def main():
    client = ConversationalSizingFitRecommenderClient()
    res = client.recommend_best_fit(180, 75, 'DENIM_JACKET')
    print('Sizing Fit Recommender: ' + res['fit_recommendation_id'] + ' (Size: ' + res['recommended_size'] + ')')
    print('Confidence: ' + str(res['confidence_score'] * 100) + '% | Return Risk: ' + str(res['predicted_return_risk_pct']) + '%')
    print('Profile URL: ' + res['fit_profile_url'])

if __name__ == '__main__':
    main()
