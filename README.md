# 1. Avantages observés
## Quels sont les avantages de l'automatisation des tests que vous avez constatés ?

- Les tests  s'exécutent en quelques secondes (voir le temps total dans report.html), ce qui est impossible à faire manuellement à cette vitesse.
- On peut lancer la même suite de tests, elle pourra toujours me renvoie la bon diagnostic à la différence d'un être humain qui peut faire des erreurs
- Si on modifie le fichier script.js pour corriger la division, les tests nous assurent immédiatement que l'addition fonctionne toujours, ce qui peut me montrer qu'il n'y a pas de problème de régréssion.

## Comment le CI/CD améliore-t-il la qualité du code ?

-Grâce au fichier ci-cd.yml, à  chaque fois qu'on push sur GitHub, cela va déclencher les tests. Si une erreur est introduite.
-Le CI tourne sur une machine propre (des runnurs qui vont faire tourner des Jobs). Cela évite le fait que cela fonctionne seulement sur une machine et pas une autre.
- On empêche de déployer une version cassée en production, car le déploiement ne peut pas avoir lieu ave des erreurs.

# 2. Défis rencontrés
## Quelles difficultés avez-vous rencontrées avec Selenium ?

- Gestion de l'environnement (Drivers) : Le problème majeur rencontré était la gestion du chromedriver (l'erreur WinError 193).
- Dans la boucle test_all_operations, le code allait parfois plus vite que le navigateur.
- La différence entre l'exécution locale (avec interface graphique) et l'exécution CI/CD (mode --headless sans interface graphique configuré dans test_selenium.py).

## Comment pourriez-vous améliorer la stabilité des tests ?

- C'est la solution que nous avons appliquée dans le code corrigé. Au lieu d'utiliser time.sleep() (ce qui peut être lent), on utilise WebDriverWait avec expected_conditions.
- Utiliser des ID uniques (By.ID) comme nous l'avons fait (num1, calculate) plutôt que des sélecteurs CSS complexes ou XPATH qui cassent au moindre changement de design.
- Utiliser des bibliothèques comme webdriver-manager à jour pour éviter les conflits de versions manuelles.

# 3. Métriques
## Quelles métriques sont les plus importantes pour votre projet ?

- Taux de succès (Pass Rate) : Le pourcentage de tests réussis (visé : 100% avant déploiement).

- Temps d'exécution : La durée totale de la suite de tests (pour ne pas ralentir le développement).

- Temps de chargement de la page : Mesuré dans votre test test_page_load_time (doit être < 3 secondes).

- Couverture de code (Code Coverage) : (Mentionné dans la partie 4.1 du TP) Savoir quel pourcentage du code source (script.js) est réellement parcouru par les tests.

## Comment mesurer l'efficacité de votre pipeline CI/CD ?

- Durée du cycle (Pipeline Duration) : Combien de temps s'écoule entre le "push" du code et le résultat final (déploiement ou rapport d'erreur).

- Fréquence des échecs (Build Failure Rate) : Si le pipeline échoue trop souvent pour des raisons techniques (pas liées au code), il est inefficace.

- MTTR (Mean Time To Recovery) : Le temps moyen nécessaire pour corriger un bug critique détecté par le pipeline.