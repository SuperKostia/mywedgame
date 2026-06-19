// Sélecteur de langue des pages utilitaires.
// Langue initiale : ?lang=en dans l'URL, sinon FR. Le bouton bascule en place
// et met à jour le paramètre d'URL (page partageable dans la bonne langue).
(function () {
  var param = new URLSearchParams(location.search).get('lang');
  if (param === 'en') document.documentElement.lang = 'en';

  function sync(l) {
    document.documentElement.lang = l;
    document.querySelectorAll('.lang-btn').forEach(function (b) {
      b.classList.toggle('active', b.dataset.lang === l);
    });
    var url = new URL(location.href);
    if (l === 'en') url.searchParams.set('lang', 'en');
    else url.searchParams.delete('lang');
    history.replaceState(null, '', url);
  }

  sync(document.documentElement.lang === 'en' ? 'en' : 'fr');

  document.querySelectorAll('.lang-btn').forEach(function (btn) {
    btn.addEventListener('click', function () { sync(btn.dataset.lang); });
  });
})();
