(() => {
  const cards = [...document.querySelectorAll('.all-grid .media-card')];
  const groupButtons = [...document.querySelectorAll('[data-filter-group]')];
  const topicButtons = [...document.querySelectorAll('[data-filter-topic]')];
  const count = document.querySelector('.results-count');
  const empty = document.querySelector('.empty-state');
  let group = 'All';
  let topic = 'All';

  const apply = () => {
    let visible = 0;
    cards.forEach(card => {
      const groupMatch = group === 'All' || card.dataset.group === group;
      const topicMatch = topic === 'All' || card.dataset.topics.split('|').includes(topic);
      card.hidden = !(groupMatch && topicMatch);
      if (!card.hidden) visible += 1;
    });
    document.querySelectorAll('.media-editorial-group').forEach(section => {
      section.hidden = ![...section.querySelectorAll('.media-card')].some(card => !card.hidden);
    });
    count.textContent = `${visible} material${visible === 1 ? '' : 's'}`;
    empty.hidden = visible !== 0;
  };

  groupButtons.forEach(button => button.addEventListener('click', () => {
    group = button.dataset.filterGroup;
    groupButtons.forEach(item => item.classList.toggle('is-active', item === button));
    apply();
  }));
  topicButtons.forEach(button => button.addEventListener('click', () => {
    topic = button.dataset.filterTopic;
    topicButtons.forEach(item => item.classList.toggle('is-active', item === button));
    apply();
  }));
  apply();
})();
