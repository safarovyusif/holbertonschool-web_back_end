export default function cleanSet(set, startString) {
  if (!startString || typeof startString !== 'string' || startString.length === 0) {
    return '';
  }
  const parts = [];
  set.forEach((value) => {
    if (value && value.startsWith(startString)) {
      parts.push(value.slice(startString.length));
    }
  });
  return parts.join('-');
}
