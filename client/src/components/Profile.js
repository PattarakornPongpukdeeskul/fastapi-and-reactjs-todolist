export const Profile = (name, medicineCount) => {
  const isSingle = medicineCount <= 1 ? 'medicine' : 'medicines'
  return (
    <div>
      <p>{`Name: ${name}`}</p>
      <p>{`To eat: ${medicineCount} ${isSingle}`}</p>
    </div>
  )
}